import sqlite3

conn = sqlite3.connect("database/siem.db")
cursor = conn.cursor()


def show_dashboard():

    print("\n========== SIEM DASHBOARD ==========\n")

    # Total Logs
    cursor.execute("SELECT COUNT(*) FROM logs")
    total_logs = cursor.fetchone()[0]

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

    print("Total Logs        :", total_logs)
    print("Successful Login  :", success)
    print("Failed Login      :", failed)

    print("\n===============================\n")