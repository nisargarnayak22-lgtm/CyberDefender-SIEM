import sqlite3

conn = sqlite3.connect("database/siem.db")
cursor = conn.cursor()

def detect_brute_force():

    cursor.execute("""
        SELECT ip, COUNT(*)
        FROM logs
        WHERE event='LOGIN_FAILED'
        GROUP BY ip
        HAVING COUNT(*) >= 3
    """)

    attacks = cursor.fetchall()

    if not attacks:
        print("\nNo Brute Force Attack Detected.")
        return

    print("\n========== BRUTE FORCE ALERT ==========\n")

    for attack in attacks:

        print("Severity : CRITICAL")
        print("Attack Type : Brute Force")
        print("IP Address :", attack[0])
        print("Failed Attempts :", attack[1])
        print("--------------------------------")