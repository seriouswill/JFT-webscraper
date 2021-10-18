import urllib
from bs4 import BeautifulSoup
url = "https://www.jftna.org/jft/index.php"


def scrape():
    with urllib.request.urlopen(url) as response:
        html = response.read()
        soup = BeautifulSoup(html)

    for script in soup(["script", "style", "a", "<div id=\"bottom\" >", "title", "meta", "htmlhead", "link", "head"]):
        script.extract()    # This rips out the tags and data inside the tags from the object

    for tags in soup(["td", "h2", "table", "tr", "body", "tr", "h1", "br", "i", "b", "tbody", "html"]):
        # This removes the tags from around the data inside, leaving just the text without tags.
        tags.unwrap()

    text = str(soup)

    # # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    print("Scraping...")
    return text


scrape()
