import smtplib, ssl

HOST = "smtp.gmail.com"
PORT = 465
PASSWORD = 'gzeljopucclxjkga'
CONTEXT = ssl.create_default_context()


def send_email(message, subject, username):
    message = f"Subject: {subject}\n" + message
    with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
        server.login(username, PASSWORD)
        server.sendmail(username, username, message)
