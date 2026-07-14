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


# =========================
# Dashboard
# =========================

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


# =========================
# Alerts Page
# =========================

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


# =========================
# User Activity Report
# =========================

@app.route("/user-report")
def user_report():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            user,
            SUM(CASE WHEN event='LOGIN_SUCCESS' THEN 1 ELSE 0 END) AS success_count,
            SUM(CASE WHEN event='LOGIN_FAILED' THEN 1 ELSE 0 END) AS failed_count,
            COUNT(*) AS total_activity
        FROM logs
        GROUP BY user
        ORDER BY total_activity DESC
    """)

    report = cursor.fetchall()

    conn.close()

    return render_template(
        "user_report.html",
        report=report
    )


# =========================
# Export CSV
# =========================

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

    writer.writerow([
        "Timestamp",
        "Event",
        "User",
        "IP Address"
    ])

    writer.writerows(rows)

    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={
            "Content-Disposition":
            "attachment; filename=siem_logs.csv"
        }
    )


# =========================
# Run Flask
# =========================
# =========================
# Security Analytics
# =========================

@app.route("/analytics")
def analytics():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    # Successful Logins
    cursor.execute("""
        SELECT COUNT(*)
        FROM logs
        WHERE event='LOGIN_SUCCESS'
    """)
    success = cursor.fetchone()[0]

    # Failed Logins
    cursor.execute("""
        SELECT COUNT(*)
        FROM logs
        WHERE event='LOGIN_FAILED'
    """)
    failed = cursor.fetchone()[0]

    # Most Targeted User
    cursor.execute("""
        SELECT user, COUNT(*)
        FROM logs
        GROUP BY user
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)
    top_user = cursor.fetchone()

    # Most Attacking IP
    cursor.execute("""
        SELECT ip, COUNT(*)
        FROM logs
        GROUP BY ip
        ORDER BY COUNT(*) DESC
        LIMIT 1
    """)
    top_ip = cursor.fetchone()

    conn.close()

    return render_template(
        "analytics.html",
        success=success,
        failed=failed,
        top_user=top_user,
        top_ip=top_ip
    )


# =========================
# Run Flask
# =========================
@app.route("/timeline")
def timeline():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT timestamp, event, user, ip
        FROM logs
        ORDER BY timestamp DESC
    """)

    logs = cursor.fetchall()

    conn.close()

    return render_template(
        "timeline.html",
        logs=logs
    )
    # =========================
# Failed Login Trends
# =========================

@app.route("/failed-login-trends")
def failed_login_trends():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            ip,
            COUNT(*) AS failed_attempts
        FROM logs
        WHERE event='LOGIN_FAILED'
        GROUP BY ip
        ORDER BY failed_attempts DESC
    """)

    trends = cursor.fetchall()

    conn.close()

    return render_template(
        "failed_login_trends.html",
        trends=trends
    )
    # =========================
# Top Active Users
# =========================

@app.route("/top-active-users")
def top_active_users():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            user,
            COUNT(*) AS total_events,
            SUM(CASE WHEN event='LOGIN_SUCCESS' THEN 1 ELSE 0 END) AS successful_logins,
            SUM(CASE WHEN event='LOGIN_FAILED' THEN 1 ELSE 0 END) AS failed_logins
        FROM logs
        GROUP BY user
        ORDER BY total_events DESC
    """)

    users = cursor.fetchall()

    conn.close()

    return render_template(
        "top_active_users.html",
        users=users
    )
    # =========================
# Event Statistics
# =========================

@app.route("/event-statistics")
def event_statistics():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            event,
            COUNT(*) AS total
        FROM logs
        GROUP BY event
        ORDER BY total DESC
    """)

    events = cursor.fetchall()

    conn.close()

    return render_template(
        "event_statistics.html",
        events=events
    )
    # =========================
# Suspicious IP Activity Report
# =========================

@app.route("/suspicious-ips")
def suspicious_ips():

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            ip,
            COUNT(*) AS failed_attempts
        FROM logs
        WHERE event='LOGIN_FAILED'
        GROUP BY ip
        HAVING COUNT(*) >= 3
        ORDER BY failed_attempts DESC
    """)

    ips = cursor.fetchall()

    conn.close()

    return render_template(
        "suspicious_ips.html",
        ips=ips
    )

if __name__ == "__main__":
    app.run(debug=True)