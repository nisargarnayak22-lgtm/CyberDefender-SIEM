from flask import Flask, render_template, request, Response
import sqlite3
import os
import csv
import io

from ip_reputation import check_ip_reputation

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

DATABASE = os.path.join(BASE_DIR, "database", "siem.db")


@app.route("/")
def dashboard():

    search = request.args.get("search", "")
    event = request.args.get("event", "")

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM logs")
    total = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE event='LOGIN_SUCCESS'")
    success = cursor.fetchone()[0]

    cursor.execute("SELECT COUNT(*) FROM logs WHERE event='LOGIN_FAILED'")
    failed = cursor.fetchone()[0]

    query = """
        SELECT timestamp,event,user,ip
        FROM logs
        WHERE user LIKE ?
    """

    params = ['%' + search + '%']

    if event:
        query += " AND event=?"
        params.append(event)

    query += " ORDER BY timestamp DESC LIMIT 10"

    cursor.execute(query, params)

    rows = cursor.fetchall()

    logs = []

    for row in rows:

        reputation = check_ip_reputation(row[3])

        logs.append((
            row[0],
            row[1],
            row[2],
            row[3],
            reputation
        ))

    conn.close()

    return render_template(
        "dashboard.html",
        total=total,
        success=success,
        failed=failed,
        logs=logs,
        search=search,
        event=event
    )


@app.route("/alerts")
def alerts():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp,user,ip,event
        FROM logs
        WHERE event='LOGIN_FAILED'
        ORDER BY timestamp DESC
        LIMIT 10
    """)

    alerts = cursor.fetchall()

    conn.close()

    return render_template(
        "alerts.html",
        alerts=alerts
    )


@app.route("/export")
def export():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp,event,user,ip
        FROM logs
        ORDER BY timestamp DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    output = io.StringIO()

    writer = csv.writer(output)

    writer.writerow(["Timestamp", "Event", "User", "IP Address"])

    writer.writerows(rows)

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=siem_logs.csv"
        }
    )


if __name__ == "__main__":
    app.run(debug=True)