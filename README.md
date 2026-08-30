# Kaizen Learning — Toyota Way Study Platform

A self-contained learning-management site: learners read a principle in depth, pass a
10-question quiz (100% required) to unlock the next one, and print a certificate once every
principle in a study set is complete. Includes user accounts, a public leaderboard ranked by
completed study sets, and an admin dashboard to monitor every learner's progress and scores.

Study Set 1 is fully built out: **The Toyota Way — 14 Management Principles**, with detailed
original explanations and 140 quiz questions (10 per principle). The platform is designed so
more study sets can be added later without touching existing user data.

## Why this stack

The build environment this was created in has no access to the npm or PyPI registries, so it
intentionally uses **only what ships with Python 3 and the Tornado web framework** (already
present): `sqlite3` for storage, `hashlib`/`hmac` (PBKDF2) for password hashing, and Tornado's
built-in templating, sessions (signed secure cookies), and web server. There is nothing to
`pip install` beyond Tornado itself, and no database server to stand up.

## Requirements

- Python 3.8+
- Tornado (`pip install tornado` — it's the only third-party dependency)

## Running it locally

```bash
cd lms
python3 app.py --port=8888
```

Then open **http://localhost:8888**.

On first run it automatically:
- creates `data/app.db` (SQLite file) and the schema,
- seeds the "Toyota's 14 Principles" study set (140 questions),
- creates a default admin account.

**Default admin login** (change the password after first login — see "Security notes" below):
```
email:    admin@lms.local
password: ChangeMe123!
```

## How it works

- **Register / Log in** — plain email + password accounts (`/register`, `/login`). Passwords
  are hashed with PBKDF2-SHA256 (200,000 iterations, random salt per user) — no plaintext or
  reversible storage.
- **Dashboard** (`/dashboard`) — every learner sees all available study sets and their
  progress bar.
- **Study set page** (`/study/<slug>`) — lists all principles for a set with lock/unlock/passed
  status. Principle 1 is always unlocked; principle *N* unlocks only once principle *N-1* has
  been passed with a perfect quiz score.
- **Principle page** (`/study/<slug>/principle/<n>`) — the detailed written explanation.
- **Quiz** (`/study/<slug>/principle/<n>/quiz`) — 10 multiple-choice questions. A learner must
  score 10/10 to unlock the next principle; otherwise they see which answers were wrong (with
  explanations) and can retake it as many times as needed.
- **Certificate** (`/study/<slug>/certificate`) — unlocked once all principles in a set are
  passed. Shows the learner's registered name and can be printed or saved as a PDF via the
  browser's print dialog (styled with dedicated print CSS).
- **Leaderboard** (`/leaderboard`) — every logged-in user can see everyone's ranking, sorted by
  number of study sets fully completed, then total principles passed.
- **Admin dashboard** (`/admin`, admin accounts only) — a monitoring view of every learner:
  principles passed, total quiz attempts, average best score, last activity, and a drill-down
  per learner per study set (`/admin/user/<id>/<slug>`) showing pass/fail and score on every
  individual principle.

## Adding another study set later

1. Create a new content module in `content/`, following the exact shape of
   `content/toyota14_principles.py`:
   - a `STUDY_SET` dict with `slug`, `title`, `description`
   - a `PRINCIPLES` list, each item with `number`, `section`, `title`, `content` (list of
     paragraph strings), and `questions` (a list of exactly 10 dicts, each with `q`,
     `options` — a list of 4 strings — `correct` — 0-based index — and `explanation`).
2. In `app.py`, import the new module near the top (next to the Toyota import) and add one
   line in `bootstrap()`:
   ```python
   dbmod.seed_study_set(NEW_STUDY_SET, NEW_PRINCIPLES)
   ```
3. Restart the server. Seeding is idempotent and additive — it will insert only the new study
   set and will not touch or duplicate existing study sets, users, or progress data.

No database migration tooling is needed for this because the schema already supports
multiple study sets; only new rows are added.

## Deploying (Netlify can't run this — here's why, and what to use instead)

**Netlify only hosts static files and short-lived serverless functions.** This app is a
long-running Python process with its own in-memory web server and a SQLite file it reads and
writes continuously — that's exactly what Netlify (and similar static hosts like GitHub Pages
or Vercel's static tier) cannot run. Rather than gut the login/leaderboard/admin features to
force it into a single static HTML file, deploy the app as-is to a host built for long-running
Python processes. Both options below have free tiers and take about 5 minutes.

The project already includes `requirements.txt`, a `Procfile`, and `render.yaml` so both hosts
below can auto-detect and run it with no extra configuration.

### Option A: Render (recommended, simplest)

1. Push the `lms/` folder to a new GitHub repository (Render deploys from a Git repo).
2. Go to [dashboard.render.com](https://dashboard.render.com) → **New +** → **Web Service** →
   connect your repo.
3. Render should auto-detect Python. Confirm:
   - **Build command:** `pip install -r requirements.txt`
   - **Start command:** `python3 app.py`
4. Under **Environment**, add two variables so you don't ship the default admin password:
   - `ADMIN_EMAIL` = your email
   - `ADMIN_PASSWORD` = a strong password
5. Click **Create Web Service**. Render gives you a live URL like
   `https://kaizen-learning.onrender.com` within a couple of minutes.

   ⚠️ **Persistence note:** Render's **free** plan has an ephemeral filesystem — the SQLite
   database (and everyone's progress) resets on every redeploy or when the free instance spins
   down from inactivity. To keep data permanently, upgrade the service to a paid plan and attach
   a **Persistent Disk** (the included `render.yaml` already requests one, mounted at
   `data/`) — Render's dashboard will prompt you to add it if you deploy via the Blueprint
   button (**New +** → **Blueprint**, pointing at this repo) instead of a plain Web Service.

### Option B: Railway

1. Push the `lms/` folder to a GitHub repository.
2. Go to [railway.app](https://railway.app) → **New Project** → **Deploy from GitHub repo**.
3. Railway auto-detects the `Procfile` and `requirements.txt` — no extra config needed.
4. Add a **Volume** (Railway's dashboard → your service → **Settings** → **Volumes**) mounted
   at `/app/data` so the SQLite file survives redeploys — Railway's free/hobby tier supports
   volumes, unlike Render's free tier.
5. Under **Variables**, add `ADMIN_EMAIL` and `ADMIN_PASSWORD` as above.
6. Railway assigns a public URL automatically under **Settings** → **Networking** → **Generate
   Domain**.

### Option C: a small VPS (DigitalOcean, Hetzner, Lightsail)

Install Python 3 + `pip install -r requirements.txt`, copy the `lms/` folder over, run
`python3 app.py` (optionally behind nginx/Caddy as a reverse proxy for TLS/HTTPS and to run it
as a system service so it restarts on reboot). The filesystem here is persistent by default —
no extra volume/disk setup needed.

For higher concurrent traffic on any of these, migrating `queries.py`/`db.py` to PostgreSQL
later is straightforward since all SQL is centralized in those two files.

## Security notes before real-world use

- Change the default admin password immediately (currently there's no in-app "change
  password" UI yet — easiest first step is deleting the `users` row and re-running
  `db.ensure_admin(password="...")` with a strong password, or adding a change-password route).
- `xsrf_cookies` is disabled in `app.py` for simplicity; if you expose this beyond a trusted
  internal audience, enable Tornado's built-in XSRF protection and add `{% raw xsrf_form_html() %}`
  to the two POST forms (login/register are safe as-is since they don't mutate other users'
  data, but the quiz-submission form should be protected in a public deployment).
- `data/cookie_secret.txt` is generated once and reused — back it up if you move servers, or
  all logged-in sessions will be invalidated (harmless, just requires re-login).
- Consider adding rate-limiting on `/login` and `/register` if opening this to the public
  internet.

## Project structure

```
lms/
  app.py                        Tornado app: routes/handlers
  db.py                         schema + password hashing + seeding
  queries.py                    all data-access + progress/ranking logic
  content/
    toyota14_principles.py      Study Set 1 content + 140 quiz questions
  templates/                    Tornado HTML templates
  static/css/style.css          green/gray "lean" visual theme
  data/                         app.db (SQLite) + cookie_secret.txt (created on first run)
  requirements.txt              pip dependency (tornado only)
  Procfile                      start command for Render/Railway/Heroku-style hosts
  render.yaml                   optional one-click Render Blueprint config
```
