from urllib.request import urlopen
from bs4 import BeautifulSoup
articleURL = "https://www.forbes.com/sites/reenitadas/2018/03/06/top-8-healthcare-predictions-for-asia/#6783062462ab"

def getTextFromUrl( url, css_content = '', xpath_content = ''):
    page = urlopen(url).read().decode('utf8')
    soup = BeautifulSoup(page,'lxml')
    text = ' '.join(map(lambda p: p.text, soup.find_all(css_content)))
    return text.encode('ascii', errors='replace')
text = getTextFromUrl( articleURL, 'article-body-container')
print(text)

