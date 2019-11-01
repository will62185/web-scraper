from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from pathlib import Path
import os

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_TO = os.getenv("EMAIL_TO")
EMAIL_PASSWORD = os.getenv("EMAIL_ADDRESS_PASSWORD")

def sendEmail(body): 
    convertedToHTML = MIMEText(body, "html")
    server = SMTP('smtp.gmail.com', 587)
    try:
        server.ehlo()
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        message = MIMEMultipart("alternative")
        message["Subject"] = "Subject: Test"
        message["From"] = EMAIL_FROM
        message["To"] = EMAIL_TO
        message.attach(convertedToHTML)
        response = server.sendmail(
            EMAIL_FROM, EMAIL_TO, message.as_string()
        )
        if response:
            f"Error: {response}"
        print('Email Sent!')
    except expression as identifier:
        f"Error: {identifier}"
    server.quit()