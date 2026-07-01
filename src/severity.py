import sqlite3

conn = sqlite3.connect("database/siem.db")
cursor = conn.cursor()

def classify_logs():

    cursor.execute("""
        SELECT timestamp,event,user,ip
        FROM logs
    """)

    logs = cursor.fetchall()

    print("\n========== LOG SEVERITY REPORT ==========\n")

    for log in logs:

        timestamp = log[0]
        event = log[1]
        user = log[2]
        ip = log[3]

        if event == "LOGIN_SUCCESS":
            severity = "LOW"

        elif event == "LOGIN_FAILED":
            severity = "HIGH"

        else:
            severity = "MEDIUM"

        print(f"Time      : {timestamp}")
        print(f"User      : {user}")
        print(f"IP        : {ip}")
        print(f"Event     : {event}")
        print(f"Severity  : {severity}")
        print("--------------------------------")