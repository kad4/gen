import pickle
import time

from bs4 import BeautifulSoup
from urllib.request import urlopen


def parser(URL):
    print("Parsing:", URL)
    try:
        currentPage = urlopen(URL).read()
        soup = BeautifulSoup(currentPage)
        if soup.rss is None:
            return parseHTML(URL, currentPage, soup)
        else:
            return parseXML(URL, currentPage, soup)
    except Exception as e:
        print('Error parsing', URL)
        print(e)


def parseHTML(URL, PAGE, SOUP):
    print("Parsing HTML")
    try:
        currentPage = PAGE
        soup = SOUP

        titles = []

        for link in soup.find_all('a'):
            titles.append([link.string, link.get('href')])

        f = open('list.lst', 'wb')
        print("written")
        pickle.dump(titles, f, protocol=pickle.HIGHEST_PROTOCOL)

        return True
    except Exception as e:
        print(e)
        return False


def parseXML(URL, PAGE, SOUP):
    print("Parsing XML")
    pageOutput = []
    try:
        currentPage = PAGE
        soup = BeautifulSoup(currentPage, 'xml')

        itemList = soup.findAll('item')
        for item in itemList:
            articleTitle = item.title.text.encode('utf-8')
            articleDate = list(time.strptime(item.pubDate.text, '%a, %d %b %Y %X %z')[:3])  # Thu, 24 Jul 2014 11:32:24 +0000
            articleURL = item.link.text
            pageOutput.append([articleTitle, articleDate, articleURL])

        return pageOutput
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    print(parser('http://localhost/gen/feed.xml'))
