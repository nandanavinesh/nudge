import sqlite3

def init_db():
    conn = sqlite3.connect('nudge.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            social_media REAL,
            productive_screen REAL,
            tasks_completed INTEGER,
            sleep_hours REAL,
            mood INTEGER,
            productivity_score REAL
        )
    ''')
    conn.commit()
    conn.close()

def save_log(date, social_media, productive_screen, tasks_completed, sleep_hours, mood):
    conn = sqlite3.connect('nudge.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO logs (date, social_media, productive_screen, tasks_completed, sleep_hours, mood)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (date, social_media, productive_screen, tasks_completed, sleep_hours, mood))
    conn.commit()
    conn.close()

def get_all_logs():
    conn = sqlite3.connect('nudge.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM logs ORDER BY date DESC')
    logs = cursor.fetchall()
    conn.close()
    return logs