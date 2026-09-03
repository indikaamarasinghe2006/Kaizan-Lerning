# -*- coding: utf-8 -*-
"""
Database layer for the Study Sets LMS.
Uses Python's built-in sqlite3 (no external dependencies).
"""
import sqlite3
import os
import hashlib
import hmac
import secrets
import datetime

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "app.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    role TEXT NOT NULL DEFAULT 'user',
    created_at TEXT NOT NULL,
    last_login TEXT
);

CREATE TABLE IF NOT EXISTS study_sets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    slug TEXT NOT NULL UNIQUE,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    sort_order INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE IF NOT EXISTS principles (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    study_set_id INTEGER NOT NULL REFERENCES study_sets(id),
    idx INTEGER NOT NULL,
    number INTEGER NOT NULL,
    section TEXT NOT NULL,
    title TEXT NOT NULL,
    content_json TEXT NOT NULL,
    UNIQUE(study_set_id, idx)
);

CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    principle_id INTEGER NOT NULL REFERENCES principles(id),
    idx INTEGER NOT NULL,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct INTEGER NOT NULL,
    explanation TEXT NOT NULL,
    UNIQUE(principle_id, idx)
);

CREATE TABLE IF NOT EXISTS progress (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id),
    principle_id INTEGER NOT NULL REFERENCES principles(id),
    passed INTEGER NOT NULL DEFAULT 0,
    best_score INTEGER NOT NULL DEFAULT 0,
    attempts INTEGER NOT NULL DEFAULT 0,
    last_attempt_at TEXT,
    passed_at TEXT,
    UNIQUE(user_id, principle_id)
);

CREATE TABLE IF NOT EXISTS certificates (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL REFERENCES users(id),
    study_set_id INTEGER NOT NULL REFERENCES study_sets(id),
    issued_at TEXT NOT NULL,
    UNIQUE(user_id, study_set_id)
);
"""


def get_conn():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn


def init_db():
    conn = get_conn()
    conn.executescript(SCHEMA)
    # Migration: older databases created before last_login existed won't have
    # the column yet — add it if missing so existing user data isn't lost.
    cols = [row["name"] for row in conn.execute("PRAGMA table_info(users)")]
    if "last_login" not in cols:
        conn.execute("ALTER TABLE users ADD COLUMN last_login TEXT")
    conn.commit()
    conn.close()


# ---------- password hashing (stdlib PBKDF2, no external deps) ----------

def hash_password(password: str, salt: bytes = None) -> str:
    if salt is None:
        salt = secrets.token_bytes(16)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)
    return salt.hex() + "$" + dk.hex()


def verify_password(password: str, stored: str) -> bool:
    try:
        salt_hex, hash_hex = stored.split("$")
    except ValueError:
        return False
    salt = bytes.fromhex(salt_hex)
    dk = hashlib.pbkdf2_hmac("sha256", password.encode("utf-8"), salt, 200_000)
    return hmac.compare_digest(dk.hex(), hash_hex)


def now_iso():
    return datetime.datetime.utcnow().isoformat(timespec="seconds") + "Z"


# ---------- seeding ----------

def seed_study_set(study_set_dict, principles_list):
    """
    Idempotent: if a study set with this slug already exists, it will NOT be
    re-inserted or duplicated. This lets new study sets be added later by
    calling this function again for the new set only, without touching
    existing user progress data.
    """
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM study_sets WHERE slug = ?", (study_set_dict["slug"],))
    row = cur.fetchone()
    if row:
        conn.close()
        return row["id"], False  # already seeded

    cur.execute("SELECT COALESCE(MAX(sort_order), -1) + 1 FROM study_sets")
    next_order = cur.fetchone()[0]

    cur.execute(
        "INSERT INTO study_sets (slug, title, description, sort_order) VALUES (?, ?, ?, ?)",
        (study_set_dict["slug"], study_set_dict["title"], study_set_dict["description"], next_order),
    )
    study_set_id = cur.lastrowid

    import json
    for idx, p in enumerate(principles_list, start=1):
        cur.execute(
            """INSERT INTO principles (study_set_id, idx, number, section, title, content_json)
               VALUES (?, ?, ?, ?, ?, ?)""",
            (study_set_id, idx, p["number"], p["section"], p["title"], json.dumps(p["content"])),
        )
        principle_id = cur.lastrowid
        for qidx, q in enumerate(p["questions"], start=1):
            opts = q["options"]
            cur.execute(
                """INSERT INTO questions
                   (principle_id, idx, question, option_a, option_b, option_c, option_d, correct, explanation)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (principle_id, qidx, q["q"], opts[0], opts[1], opts[2], opts[3], q["correct"], q["explanation"]),
            )

    conn.commit()
    conn.close()
    return study_set_id, True


def record_login(user_id):
    """Stamp the current time as this user's most recent successful login."""
    conn = get_conn()
    conn.execute("UPDATE users SET last_login = ? WHERE id = ?", (now_iso(), user_id))
    conn.commit()
    conn.close()


def ensure_admin(name="Site Admin", email="admin@lms.local", password="ChangeMe123!"):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id FROM users WHERE email = ?", (email,))
    if cur.fetchone():
        conn.close()
        return
    cur.execute(
        "INSERT INTO users (name, email, password_hash, role, created_at) VALUES (?, ?, ?, 'admin', ?)",
        (name, email, hash_password(password), now_iso()),
    )
    conn.commit()
    conn.close()
