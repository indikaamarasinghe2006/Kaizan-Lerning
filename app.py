# -*- coding: utf-8 -*-
"""
Toyota Way Learning Platform
A self-contained study-set LMS: read a principle, pass a 10-question quiz
(100% required) to unlock the next one, track progress, show a leaderboard,
give admins a monitoring dashboard, and issue a printable certificate on
completion.

Runs on Tornado + sqlite3 only (Python standard library + Tornado, both
already available — no extra network installs required).

Run:
    python3 app.py --port=8888

Default admin login:
    email:    admin@lms.local
    password: ChangeMe123!   (CHANGE THIS after first login in a real deployment)
"""
import os
import json
import logging
import secrets

import tornado.ioloop
import tornado.web
from tornado.options import define, options, parse_command_line

import db as dbmod
import queries as q
from content.toyota14_principles import STUDY_SET as TOYOTA_STUDY_SET, PRINCIPLES as TOYOTA_PRINCIPLES

define("port", default=8888, help="run on the given port", type=int)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR, "data", "cookie_secret.txt")


def get_or_create_cookie_secret():
    os.makedirs(os.path.dirname(SECRET_FILE), exist_ok=True)
    if os.path.exists(SECRET_FILE):
        with open(SECRET_FILE, "r") as f:
            return f.read().strip()
    secret = secrets.token_hex(32)
    with open(SECRET_FILE, "w") as f:
        f.write(secret)
    return secret


class BaseHandler(tornado.web.RequestHandler):
    def get_current_user(self):
        uid = self.get_secure_cookie("user_id")
        if not uid:
            return None
        user = q.get_user_by_id(int(uid.decode("utf-8")))
        return user

    def render(self, template_name, **kwargs):
        kwargs.setdefault("error", None)
        kwargs.setdefault("message", None)
        super().render(template_name, **kwargs)

    def require_login(self):
        if not self.current_user:
            self.redirect("/login")
            return False
        return True

    def require_admin(self):
        if not self.current_user or self.current_user["role"] != "admin":
            self.set_status(403)
            self.render("error.html", title="Forbidden",
                         detail="You do not have permission to view this page.")
            return False
        return True


class HomeHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.redirect("/dashboard")
            return
        self.render("home.html")


class RegisterHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.redirect("/dashboard")
            return
        self.render("register.html")

    def post(self):
        name = self.get_body_argument("name", "").strip()
        email = self.get_body_argument("email", "").strip().lower()
        password = self.get_body_argument("password", "")
        confirm = self.get_body_argument("confirm", "")

        if not name or not email or not password:
            self.render("register.html", error="Please fill in all fields.")
            return
        if password != confirm:
            self.render("register.html", error="Passwords do not match.")
            return
        if len(password) < 6:
            self.render("register.html", error="Password must be at least 6 characters.")
            return
        if q.get_user_by_email(email):
            self.render("register.html", error="An account with that email already exists.")
            return

        uid = q.create_user(name, email, password)
        self.set_secure_cookie("user_id", str(uid))
        self.redirect("/dashboard")


class LoginHandler(BaseHandler):
    def get(self):
        if self.current_user:
            self.redirect("/dashboard")
            return
        self.render("login.html")

    def post(self):
        email = self.get_body_argument("email", "").strip().lower()
        password = self.get_body_argument("password", "")
        user = q.get_user_by_email(email)
        if not user or not dbmod.verify_password(password, user["password_hash"]):
            logging.warning(f"Login failed for {email} from {self.request.remote_ip}")
            self.render("login.html", error="Invalid email or password.")
            return
        dbmod.record_login(user["id"])
        logging.info(
            f"Login success: {user['email']} (id={user['id']}, role={user['role']}) "
            f"from {self.request.remote_ip}"
        )
        self.set_secure_cookie("user_id", str(user["id"]))
        if user["role"] == "admin":
            self.redirect("/admin")
        else:
            self.redirect("/dashboard")


class LogoutHandler(BaseHandler):
    def get(self):
        self.clear_cookie("user_id")
        self.redirect("/")


class DashboardHandler(BaseHandler):
    def get(self):
        if not self.require_login():
            return
        study_sets = q.list_study_sets()
        summaries = []
        for ss in study_sets:
            principles = q.list_principles(ss["id"])
            progress_map = q.get_progress_map(self.current_user["id"], ss["id"])
            passed_count = sum(1 for p in principles if progress_map.get(p["id"]) and progress_map[p["id"]]["passed"])
            summaries.append({
                "study_set": ss,
                "total": len(principles),
                "passed": passed_count,
                "complete": len(principles) > 0 and passed_count == len(principles),
            })
        self.render("dashboard.html", summaries=summaries)


class StudySetHandler(BaseHandler):
    def get(self, slug):
        if not self.require_login():
            return
        ss = q.get_study_set_by_slug(slug)
        if not ss:
            raise tornado.web.HTTPError(404)
        principles = q.list_principles(ss["id"])
        progress_map = q.get_progress_map(self.current_user["id"], ss["id"])
        rows = []
        for p in principles:
            unlocked = q.is_principle_unlocked(
                self.current_user["id"], ss["id"], p["idx"], progress_map, principles
            )
            prog = progress_map.get(p["id"])
            rows.append({
                "principle": p,
                "unlocked": unlocked,
                "passed": bool(prog and prog["passed"]),
                "best_score": prog["best_score"] if prog else None,
            })
        complete = len(principles) > 0 and all(r["passed"] for r in rows)
        self.render("study_set.html", study_set=ss, rows=rows, complete=complete)


class PrincipleHandler(BaseHandler):
    def get(self, slug, idx):
        if not self.require_login():
            return
        idx = int(idx)
        ss = q.get_study_set_by_slug(slug)
        if not ss:
            raise tornado.web.HTTPError(404)
        principle = q.get_principle(ss["id"], idx)
        if not principle:
            raise tornado.web.HTTPError(404)
        principles = q.list_principles(ss["id"])
        progress_map = q.get_progress_map(self.current_user["id"], ss["id"])
        unlocked = q.is_principle_unlocked(self.current_user["id"], ss["id"], idx, progress_map, principles)
        if not unlocked:
            self.render("error.html", title="Locked",
                         detail="You need to pass the previous principle's quiz before viewing this one.")
            return
        prog = progress_map.get(principle["id"])
        content_paragraphs = json.loads(principle["content_json"])
        self.render(
            "principle.html",
            study_set=ss,
            principle=principle,
            content_paragraphs=content_paragraphs,
            passed=bool(prog and prog["passed"]),
            best_score=prog["best_score"] if prog else None,
            total_principles=len(principles),
            is_last=(idx == len(principles)),
        )


class QuizHandler(BaseHandler):
    def _load(self, slug, idx):
        idx = int(idx)
        ss = q.get_study_set_by_slug(slug)
        if not ss:
            raise tornado.web.HTTPError(404)
        principle = q.get_principle(ss["id"], idx)
        if not principle:
            raise tornado.web.HTTPError(404)
        principles = q.list_principles(ss["id"])
        progress_map = q.get_progress_map(self.current_user["id"], ss["id"])
        unlocked = q.is_principle_unlocked(self.current_user["id"], ss["id"], idx, progress_map, principles)
        return ss, principle, principles, unlocked

    def get(self, slug, idx):
        if not self.require_login():
            return
        ss, principle, principles, unlocked = self._load(slug, idx)
        if not unlocked:
            self.render("error.html", title="Locked",
                         detail="You need to pass the previous principle's quiz before taking this one.")
            return
        questions = q.get_questions(principle["id"])
        self.render("quiz.html", study_set=ss, principle=principle, questions=questions, result=None)

    def post(self, slug, idx):
        if not self.require_login():
            return
        ss, principle, principles, unlocked = self._load(slug, idx)
        if not unlocked:
            self.render("error.html", title="Locked",
                         detail="You need to pass the previous principle's quiz before taking this one.")
            return
        questions = q.get_questions(principle["id"])
        total = len(questions)
        score = 0
        details = []
        for question in questions:
            field = f"q_{question['id']}"
            answer_raw = self.get_body_argument(field, None)
            answer = int(answer_raw) if answer_raw is not None else None
            is_correct = (answer == question["correct"])
            if is_correct:
                score += 1
            details.append({
                "question": question,
                "selected": answer,
                "is_correct": is_correct,
            })
        passed = (score == total and total > 0)
        q.record_attempt(self.current_user["id"], principle["id"], score, total, passed)

        next_idx = principle["idx"] + 1
        has_next = next_idx <= len(principles)
        result = {
            "score": score,
            "total": total,
            "passed": passed,
            "details": details,
            "has_next": has_next,
            "next_idx": next_idx,
            "is_last": not has_next,
        }
        if passed and not has_next:
            q.issue_certificate_if_eligible(self.current_user["id"], ss["id"])
        self.render("quiz.html", study_set=ss, principle=principle, questions=questions, result=result)


class CertificateHandler(BaseHandler):
    def get(self, slug):
        if not self.require_login():
            return
        ss = q.get_study_set_by_slug(slug)
        if not ss:
            raise tornado.web.HTTPError(404)
        if not q.is_study_set_complete(self.current_user["id"], ss["id"]):
            self.render("error.html", title="Not yet complete",
                         detail="Finish all principles in this study set to unlock your certificate.")
            return
        cert = q.issue_certificate_if_eligible(self.current_user["id"], ss["id"])
        self.render("certificate.html", study_set=ss, cert=cert, user=self.current_user)


class LeaderboardHandler(BaseHandler):
    def get(self):
        if not self.require_login():
            return
        board = q.compute_leaderboard()
        self.render("leaderboard.html", board=board, current_user_id=self.current_user["id"])


class AdminHandler(BaseHandler):
    def get(self):
        if not self.require_login():
            return
        if not self.require_admin():
            return
        overview = q.admin_user_overview()
        study_sets = q.list_study_sets()
        board = q.compute_leaderboard()
        self.render("admin.html", overview=overview, study_sets=study_sets, board=board)


class AdminUserDetailHandler(BaseHandler):
    def get(self, user_id, slug):
        if not self.require_login():
            return
        if not self.require_admin():
            return
        user_id = int(user_id)
        target = q.get_user_by_id(user_id)
        ss = q.get_study_set_by_slug(slug)
        if not target or not ss:
            raise tornado.web.HTTPError(404)
        detail = q.admin_user_detail(user_id, ss["id"])
        self.render("admin_user_detail.html", target=target, study_set=ss, detail=detail)


class ErrorHandler404(BaseHandler):
    def prepare(self):
        self.set_status(404)
        self.render("error.html", title="Not found", detail="That page does not exist.")


def make_app():
    settings = {
        "template_path": os.path.join(BASE_DIR, "templates"),
        "static_path": os.path.join(BASE_DIR, "static"),
        "cookie_secret": get_or_create_cookie_secret(),
        "login_url": "/login",
        "xsrf_cookies": False,  # simple forms-only app; enable + add xsrf tokens for production hardening
        "default_handler_class": ErrorHandler404,
    }
    return tornado.web.Application([
        (r"/", HomeHandler),
        (r"/register", RegisterHandler),
        (r"/login", LoginHandler),
        (r"/logout", LogoutHandler),
        (r"/dashboard", DashboardHandler),
        (r"/leaderboard", LeaderboardHandler),
        (r"/admin", AdminHandler),
        (r"/admin/user/([0-9]+)/([a-z0-9\-]+)", AdminUserDetailHandler),
        (r"/study/([a-z0-9\-]+)", StudySetHandler),
        (r"/study/([a-z0-9\-]+)/principle/([0-9]+)", PrincipleHandler),
        (r"/study/([a-z0-9\-]+)/principle/([0-9]+)/quiz", QuizHandler),
        (r"/study/([a-z0-9\-]+)/certificate", CertificateHandler),
    ], **settings)


def bootstrap():
    dbmod.init_db()
    q.list_study_sets()  # touch to ensure db file exists
    sid, created = dbmod.seed_study_set(TOYOTA_STUDY_SET, TOYOTA_PRINCIPLES)
    if created:
        print(f"Seeded study set '{TOYOTA_STUDY_SET['title']}' (id={sid})")
    # Allow overriding the seeded admin account via environment variables so a
    # production deploy (Render/Railway) doesn't have to ship with the default
    # password. Only used the very first time the admin row is created.
    admin_email = os.environ.get("ADMIN_EMAIL", "admin@lms.local")
    admin_password = os.environ.get("ADMIN_PASSWORD", "ChangeMe123!")
    dbmod.ensure_admin(email=admin_email, password=admin_password)


if __name__ == "__main__":
    parse_command_line()
    bootstrap()
    app = make_app()
    # Render / Railway / Heroku-style hosts inject the port to bind via the PORT
    # env var. Fall back to --port (default 8888) for local development.
    port = int(os.environ.get("PORT", options.port))
    # xheaders=True makes Tornado trust the X-Forwarded-For / X-Forwarded-Proto
    # headers set by Render's proxy, so self.request.remote_ip is the real
    # visitor IP instead of the proxy's internal address.
    app.listen(port, address="0.0.0.0", xheaders=True)
    print(f"Toyota Way Learning Platform running on http://0.0.0.0:{port}")
    print(f"Admin login -> email: {os.environ.get('ADMIN_EMAIL', 'admin@lms.local')} "
          f"| password: {'(set via ADMIN_PASSWORD env var)' if 'ADMIN_PASSWORD' in os.environ else 'ChangeMe123!'}")
    tornado.ioloop.IOLoop.current().start()
