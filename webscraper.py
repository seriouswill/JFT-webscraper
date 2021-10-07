import ssl
import smtplib
import urllib
from bs4 import BeautifulSoup
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
# get text
#text = soup.select('.C_doc')[0].get_text()
#text = soup.select('.content')[0].get_text()

# if soup.select('td'):
#     text = soup.select('td')[0].get_text()
# else:
#     text = soup.select('i')[0].get_text()

# # break into lines and remove leading and trailing space on each
# lines = (line.strip() for line in text.splitlines())
# # break multi-headlines into a line each
# chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# # drop blank lines
# text = '\n'.join(chunk for chunk in chunks if chunk)


td_tag = soup.td
h2_tag = soup.h2
# td_tag.unwrap()
# h2_tag.unwrap()


# for text_x in text:
#     print(text_x)

# text = text.strip()

print(text)


# fo = open('foo.txt', 'w')
# fo.seek(0, 2)
# line = fo.writelines(text)
# fo.close()
# writing done :)
