from src.log_collector import collect_logs
from src.parser import parse_log
from src.database import insert_log, clear_logs
from src.detector import detect_failed_logins

clear_logs()

logs = collect_logs("logs/system.log")

for log in logs:

    parsed = parse_log(log)

    insert_log(parsed)

    print("Stored:", parsed)

print("\nRunning Threat Detection...\n")

detect_failed_logins()