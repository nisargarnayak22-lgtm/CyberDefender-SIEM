import sqlite3

conn = sqlite3.connect("database/siem.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS logs(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    event TEXT,
    user TEXT,
    ip TEXT
)
""")

conn.commit()


def insert_log(log):
    cursor.execute("""
    INSERT INTO logs(timestamp,event,user,ip)
    VALUES(?,?,?,?)
    """,
    (
        log["timestamp"],
        log["event"],
        log["user"],
        log["ip"]
    ))

    conn.commit()


# NEW FUNCTION
def clear_logs():
    cursor.execute("DELETE FROM logs")
    conn.commit()