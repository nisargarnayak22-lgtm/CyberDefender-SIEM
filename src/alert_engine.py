import csv
import os

def save_alert(alert):

    file_exists = os.path.exists("alerts/alerts.csv")

    with open(
        "alerts/alerts.csv",
        "a",
        newline=""
    ) as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Severity",
                "Message"
            ])

        writer.writerow([
            alert["severity"],
            alert["message"]
        ])