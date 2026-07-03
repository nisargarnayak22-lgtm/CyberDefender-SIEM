from flask import Flask, render_template
import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)

DATABASE = os.path.join(BASE_DIR, "database", "siem.db")


@app.route("/")
def dashboard():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM logs")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE event='LOGIN_SUCCESS'")
    success = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE event='LOGIN_FAILED'")
    failed = cursor.fetchone()[0]

    cursor.execute("""
        SELECT timestamp, event, user, ip
        FROM logs
        ORDER BY timestamp DESC
    """)

    logs = cursor.fetchall()
    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        success=success,
        failed=failed,
        logs=logs
    )


if __name__ == "__main__":
    app.run(debug=True)