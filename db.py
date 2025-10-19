import sqlite3

DB_FILE = "poems.db"

# ---------- Database Setup ----------
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS poems (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    author TEXT NOT NULL,
                    title TEXT NOT NULL,
                    content TEXT NOT NULL
                )''')
    conn.commit()
    conn.close()

# ---------- Load all poems ----------
def load_poems():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT author, title, content FROM poems ORDER BY id DESC")
    poems = [{"author": row[0], "title": row[1], "content": row[2]} for row in c.fetchall()]
    conn.close()
    return poems

# ---------- Save a new poem ----------
def save_poem(poem):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO poems (author, title, content) VALUES (?, ?, ?)",
              (poem["author"], poem["title"], poem["content"]))
    conn.commit()
    conn.close()

# Initialize database when imported
init_db()
