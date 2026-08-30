# -*- coding: utf-8 -*-
"""
Query helpers: progress tracking, unlock logic, ranking/leaderboard, admin views.
Built on top of db.get_conn(). Kept as plain functions (no ORM) for clarity.
"""
import json
import db as dbmod


def get_user_by_email(email):
    conn = dbmod.get_conn()
    row = conn.execute("SELECT * FROM users WHERE email = ?", (email,)).fetchone()
    conn.close()
    return row


def get_user_by_id(user_id):
    conn = dbmod.get_conn()
    row = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    return row


def create_user(name, email, password):
    conn = dbmod.get_conn()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO users (name, email, password_hash, role, created_at) VALUES (?, ?, ?, 'user', ?)",
        (name, email, dbmod.hash_password(password), dbmod.now_iso()),
    )
    conn.commit()
    uid = cur.lastrowid
    conn.close()
    return uid


def list_study_sets():
    conn = dbmod.get_conn()
    rows = conn.execute("SELECT * FROM study_sets ORDER BY sort_order").fetchall()
    conn.close()
    return rows


def get_study_set_by_slug(slug):
    conn = dbmod.get_conn()
    row = conn.execute("SELECT * FROM study_sets WHERE slug = ?", (slug,)).fetchone()
    conn.close()
    return row


def list_principles(study_set_id):
    conn = dbmod.get_conn()
    rows = conn.execute(
        "SELECT * FROM principles WHERE study_set_id = ? ORDER BY idx", (study_set_id,)
    ).fetchall()
    conn.close()
    return rows


def get_principle(study_set_id, idx):
    conn = dbmod.get_conn()
    row = conn.execute(
        "SELECT * FROM principles WHERE study_set_id = ? AND idx = ?", (study_set_id, idx)
    ).fetchone()
    conn.close()
    return row


def get_principle_by_id(principle_id):
    conn = dbmod.get_conn()
    row = conn.execute("SELECT * FROM principles WHERE id = ?", (principle_id,)).fetchone()
    conn.close()
    return row


def get_questions(principle_id):
    conn = dbmod.get_conn()
    rows = conn.execute(
        "SELECT * FROM questions WHERE principle_id = ? ORDER BY idx", (principle_id,)
    ).fetchall()
    conn.close()
    return rows


def get_progress_map(user_id, study_set_id):
    """Return {principle_id: progress_row} for all principles in a study set."""
    conn = dbmod.get_conn()
    rows = conn.execute(
        """SELECT pr.* FROM progress pr
           JOIN principles p ON p.id = pr.principle_id
           WHERE pr.user_id = ? AND p.study_set_id = ?""",
        (user_id, study_set_id),
    ).fetchall()
    conn.close()
    return {r["principle_id"]: r for r in rows}


def is_principle_unlocked(user_id, study_set_id, idx, progress_map=None, principles=None):
    """Principle 1 is always unlocked. Principle N unlocked iff N-1 has passed=1."""
    if idx <= 1:
        return True
    if principles is None:
        principles = list_principles(study_set_id)
    if progress_map is None:
        progress_map = get_progress_map(user_id, study_set_id)
    prev = next((p for p in principles if p["idx"] == idx - 1), None)
    if prev is None:
        return False
    prog = progress_map.get(prev["id"])
    return bool(prog and prog["passed"])


def record_attempt(user_id, principle_id, score, total, passed):
    conn = dbmod.get_conn()
    cur = conn.cursor()
    existing = cur.execute(
        "SELECT * FROM progress WHERE user_id = ? AND principle_id = ?", (user_id, principle_id)
    ).fetchone()
    now = dbmod.now_iso()
    if existing:
        best = max(existing["best_score"], score)
        already_passed = bool(existing["passed"])
        new_passed = already_passed or passed
        passed_at = existing["passed_at"] if already_passed else (now if passed else None)
        cur.execute(
            """UPDATE progress SET passed=?, best_score=?, attempts=attempts+1,
               last_attempt_at=?, passed_at=? WHERE user_id=? AND principle_id=?""",
            (1 if new_passed else 0, best, now, passed_at, user_id, principle_id),
        )
    else:
        cur.execute(
            """INSERT INTO progress (user_id, principle_id, passed, best_score, attempts,
               last_attempt_at, passed_at) VALUES (?, ?, ?, ?, 1, ?, ?)""",
            (user_id, principle_id, 1 if passed else 0, score, now, now if passed else None),
        )
    conn.commit()
    conn.close()


def is_study_set_complete(user_id, study_set_id):
    principles = list_principles(study_set_id)
    if not principles:
        return False
    progress_map = get_progress_map(user_id, study_set_id)
    return all(bool(progress_map.get(p["id"]) and progress_map[p["id"]]["passed"]) for p in principles)


def issue_certificate_if_eligible(user_id, study_set_id):
    if not is_study_set_complete(user_id, study_set_id):
        return None
    conn = dbmod.get_conn()
    cur = conn.cursor()
    existing = cur.execute(
        "SELECT * FROM certificates WHERE user_id=? AND study_set_id=?", (user_id, study_set_id)
    ).fetchone()
    if existing:
        conn.close()
        return existing
    cur.execute(
        "INSERT INTO certificates (user_id, study_set_id, issued_at) VALUES (?, ?, ?)",
        (user_id, study_set_id, dbmod.now_iso()),
    )
    conn.commit()
    cert = cur.execute(
        "SELECT * FROM certificates WHERE user_id=? AND study_set_id=?", (user_id, study_set_id)
    ).fetchone()
    conn.close()
    return cert


# ---------- Ranking / Leaderboard ----------

def compute_leaderboard():
    """
    Returns a list of dicts sorted by (sets_completed desc, principles_completed desc, name asc):
    {user_id, name, email, sets_completed, principles_completed, total_principles}
    """
    conn = dbmod.get_conn()
    users = conn.execute("SELECT id, name, email FROM users WHERE role != 'admin'").fetchall()
    study_sets = conn.execute("SELECT id FROM study_sets").fetchall()
    total_principles_all = conn.execute("SELECT COUNT(*) c FROM principles").fetchone()["c"]

    # principle counts per study set
    set_principle_counts = {}
    for ss in study_sets:
        c = conn.execute(
            "SELECT COUNT(*) c FROM principles WHERE study_set_id = ?", (ss["id"],)
        ).fetchone()["c"]
        set_principle_counts[ss["id"]] = c

    results = []
    for u in users:
        passed_rows = conn.execute(
            """SELECT p.study_set_id AS set_id, COUNT(*) AS cnt
               FROM progress pr JOIN principles p ON p.id = pr.principle_id
               WHERE pr.user_id = ? AND pr.passed = 1
               GROUP BY p.study_set_id""",
            (u["id"],),
        ).fetchall()
        passed_by_set = {r["set_id"]: r["cnt"] for r in passed_rows}
        principles_completed = sum(passed_by_set.values())
        sets_completed = sum(
            1 for sid, cnt in passed_by_set.items()
            if set_principle_counts.get(sid, -1) > 0 and cnt >= set_principle_counts[sid]
        )
        results.append({
            "user_id": u["id"],
            "name": u["name"],
            "email": u["email"],
            "sets_completed": sets_completed,
            "principles_completed": principles_completed,
            "total_principles": total_principles_all,
        })
    conn.close()
    results.sort(key=lambda r: (-r["sets_completed"], -r["principles_completed"], r["name"].lower()))
    return results


def admin_user_overview():
    """Detailed per-user stats for the admin monitoring dashboard."""
    conn = dbmod.get_conn()
    users = conn.execute(
        "SELECT id, name, email, created_at FROM users WHERE role != 'admin' ORDER BY name"
    ).fetchall()
    overview = []
    for u in users:
        attempts_row = conn.execute(
            "SELECT COALESCE(SUM(attempts),0) a, COALESCE(AVG(best_score),0) avgscore, COUNT(*) touched "
            "FROM progress WHERE user_id = ?",
            (u["id"],),
        ).fetchone()
        passed = conn.execute(
            "SELECT COUNT(*) c FROM progress WHERE user_id = ? AND passed = 1", (u["id"],)
        ).fetchone()["c"]
        last_activity = conn.execute(
            "SELECT MAX(last_attempt_at) m FROM progress WHERE user_id = ?", (u["id"],)
        ).fetchone()["m"]
        overview.append({
            "id": u["id"],
            "name": u["name"],
            "email": u["email"],
            "joined": u["created_at"],
            "principles_passed": passed,
            "total_attempts": attempts_row["a"],
            "avg_best_score": round(attempts_row["avgscore"], 1),
            "last_activity": last_activity or "—",
        })
    conn.close()
    return overview


def admin_user_detail(user_id, study_set_id):
    """Per-principle pass/fail/score detail for one user in one study set (for admin drill-down)."""
    principles = list_principles(study_set_id)
    progress_map = get_progress_map(user_id, study_set_id)
    detail = []
    for p in principles:
        prog = progress_map.get(p["id"])
        detail.append({
            "number": p["number"],
            "title": p["title"],
            "passed": bool(prog and prog["passed"]),
            "best_score": prog["best_score"] if prog else 0,
            "attempts": prog["attempts"] if prog else 0,
        })
    return detail
