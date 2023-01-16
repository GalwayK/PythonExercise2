import smtplib, ssl
import os

HOST = "smtp.gmail.com"
MY_EMAIL = "kyligalway@gmail.com"
PORT = 465
PASSWORD = os.getenv("PASSWORD")
CONTEXT = ssl.create_default_context()


def send_email(message, subject, username):
    message = f"""\
Subject: {subject} 

Message From: {username}:
{message}
"""
    with smtplib.SMTP_SSL(HOST, PORT, context=CONTEXT) as server:
        server.login(MY_EMAIL, PASSWORD)
        server.sendmail(username, MY_EMAIL, message)
