from src.log_collector import collect_logs
from src.parser import parse_log
from src.database import insert_log
from src.detector import detect_failed_logins
from src.alert_engine import save_alert
from src.dashboard import show_dashboard
from src.brute_force import detect_brute_force

logs = collect_logs("logs/system.log")

for log in logs:

    parsed = parse_log(log)

    insert_log(parsed)

    print("Stored:", parsed)

print("\nRunning Threat Detection...\n")

alert = detect_failed_logins()

if alert:
    save_alert(alert)
    print("\nAlert saved successfully!")
    show_dashboard()
    detect_brute_force()