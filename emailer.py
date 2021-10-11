import schedule
import time

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
import os

import ssl
import smtplib
import urllib
from bs4 import BeautifulSoup


def scrape():

    url = "https://www.jftna.org/jft/index.php"

    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html)

    # kill all script and style elements
    for script in soup(["script", "style", "a", "<div id=\"bottom\" >", "title", "meta", "htmlhead", "link", "head"]):
        script.extract()    # rip it out

    for tags in soup(["td", "h2", "table", "tr", "body", "tr", "h1", "br", "i", "b", "tbody", "html"]):
        tags.unwrap()
    text = soup

    # # break into lines and remove leading and trailing space on each
    # lines = (line.strip() for line in text.splitlines())
    # # break multi-headlines into a line each
    # chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # # drop blank lines
    # text = '\n'.join(chunk for chunk in chunks if chunk)

    # havent got these formatting elements quite right yet

    td_tag = soup.td
    h2_tag = soup.h2

    return text

    # fo = open('foo.txt', 'w')
    # fo.seek(0, 2)
    # line = fo.writelines(text)
    # fo.close()
    # writing done :)
print(scrape())


def mail():
    global text
    smtp = smtplib.SMTP('smtp.gmail.com', 587)
    smtp.ehlo()
    smtp.starttls()
    smtp.login('justfortodaytester@gmail.com', '!!Password123')

    msg = MIMEMultipart()
    msg['Subject'] = "Just For Today"
    msg.attach(MIMEText(scrape))

    to = ["williamjamesoc@gmail.com", "thelise.rocquin@gmail.com"]
    smtp.sendmail(from_addr="justfortodaytester@gmail.com",
                  to_addrs=to, msg=msg.as_string())
    print("Sending...")
    smtp.quit()


schedule.every().day.at("09:28").do(scrape)

schedule.every().day.at("09:30").do(mail)

while True:
    schedule.run_pending()
    time.sleep(5)
