import sqlite3

conn = sqlite3.connect("database/siem.db")

cursor = conn.cursor()


def detect_failed_logins():

    cursor.execute("""
    SELECT timestamp,event,user,ip
    FROM logs
    WHERE event='LOGIN_FAILED'
    """)

    failed_logs = cursor.fetchall()

    if not failed_logs:
        print("No failed login attempts detected.")
        return None

    print("\n========== SECURITY ALERT ==========\n")

    for log in failed_logs:

        print(f"Time : {log[0]}")
        print(f"User : {log[2]}")
        print(f"IP   : {log[3]}")
        print("Event: LOGIN_FAILED")
        print("--------------------------------")

    print("Total Failed Logins:", len(failed_logs))

    return {
        "severity": "High",
        "message": f"{len(failed_logs)} failed login attempts detected."
    }