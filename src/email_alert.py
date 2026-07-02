import smtplib
from email.message import EmailMessage

SENDER_EMAIL = "nisarganayak290@gmail.com"
APP_PASSWORD = "drdjvsghorcnhpkg"
RECEIVER_EMAIL = "nisarganayak290@gmail.com"


def send_email_alert(subject, body):

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)

    print("Email Alert Sent Successfully!")