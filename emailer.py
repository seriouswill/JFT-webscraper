import schedule
import time

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os


from webscraper import text


def mail():
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('justfortodaytester@gmail.com', '!!Password123')

    msg = MIMEMultipart()
    msg['Subject'] = "Just For Today"
    msg.attach(MIMEText(text))

    to = ["williamjamesoc@gmail.com"]
    smtp.sendmail(from_addr="justfortodaytester@gmail.com",
                  to_addrs=to, msg=msg.as_string())
    print("Sending...")
    smtp.quit()


schedule.every().day.at("11:13").do(mail)

while True:
    schedule.run_pending()
    time.sleep(5)
