def collect_logs(file_path):
    try:
        with open(file_path, "r") as file:
            logs = file.readlines()
        return logs
    except FileNotFoundError:
        print("Log file not found")
        return []