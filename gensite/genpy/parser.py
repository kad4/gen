import re
import time
import urllib.request

from bs4 import BeautifulSoup
from urllib.parse import urlparse
from urllib.request import urlopen


def parser(URL):
    opener = urllib.request.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    urllib.request.install_opener(opener)
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

        netloc = urlparse(URL).netloc.split('.')
        if 'ratopati' in netloc or 'onlinekhabar' in netloc:
            item = soup.find('div', id='sing_cont')
            itemText = item.findAll('p')
            TextItem = [paras for paras in itemText]
        elif 'setopati' in netloc:
            item = soup.find('div', id='newsbox')
            itemText = item.findAll('div', class_=False)
            TextItem = [paras for paras in itemText]
        elif 'bbc' in netloc:
            item = soup.find('div', class_='bodytext')
            itemText = item.findAll(re.compile('p|h2'))
            TextItem = [paras for paras in itemText]
            for paras in TextItem:
                print (paras.encode('utf-8'),'|||',paras.parent.encode('utf-8'))
                if paras.parent != item:
                    TextItem.remove(paras)
        return TextItem
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
    text = parser('http://www.bbc.co.uk/nepali/news/2014/06/140602_ucpn_maoist_brb.shtml')
    for sT in text:
        # print(sT.encode('utf-8'))
        pass