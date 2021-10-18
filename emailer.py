import schedule
import time

from email.mime.text import MIMEText                # for text in email
from email.mime.image import MIMEImage              # for images in email
from email.mime.multipart import MIMEMultipart
import smtplib

from webscraper import scrape


def mail():

    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('justfortodaytester@gmail.com', '!!Password123')

    msg = MIMEMultipart()
    msg['Subject'] = "Just For Today"
    msg.attach(MIMEText(scrape()))
    to = ["williamjamesoc@gmail.com", "josefsquire@gmail.com"]
    smtp.sendmail(from_addr="justfortodaytester@gmail.com",
                  to_addrs=to, msg=msg.as_string())
    print("Sending...")
    smtp.quit()


schedule.every().day.at("09:30").do(scrape)
schedule.every().day.at("09:30").do(mail)


while True:
    schedule.run_pending()
    time.sleep(5)
