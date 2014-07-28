import pickle
import re
import threading
import urllib.request

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen


class sitecrawler:

    def __init__(self, sites):

        self.__doc__ = "Crawls given website and searches for articles. Articles are stored in self.Articles and all visited URLs are stored in self.URLs"

        self.sourceURLs = sites
        self.fileInUse = 0
        self.sitesCrawled = 0
        self.URLs = []
        self.Articles = []

        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]
        urllib.request.install_opener(opener)

    def crawler(self, URL):
        # Crawler initialisation
        articleURL = []
        currentList = [URL]
        visitedList = self.URLs + currentList

        parsedURL = urlparse(URL)
        print("Crawling", parsedURL.netloc)

        errorCount = 0

        # Beginning crawler loop
        while currentList.__len__() > 0:  # and visitedList.__len__() < 20:
            url = currentList.pop(0)
            if urlparse(url).netloc != urlparse(URL).netloc:
                continue
            print("Current URL:", url[0:100])
            try:
                currentPage = urlopen(url).read()
                soup = BeautifulSoup(currentPage)
            except Exception as e:
                print('Error loading', url[0:100])
                print(e)
                errorCount += 1
                continue

            if url not in visitedList:
                # Updating visited URL list and article list
                articleResult = self.isArticle(url, soup)
                if articleResult[0] is True:
                    articleURL.append(articleResult[1:])
                visitedList.append(url)

            soupLinks = soup.findAll("a", href=True)

            for soupLink in soupLinks:
                tempURL = urljoin(url, soupLink['href'])

                reTempURL = re.findall(r'(.*)#.*', tempURL)

                if reTempURL != []:
                    tempURL = reTempURL[0]

                if tempURL not in visitedList and tempURL not in currentList:
                    currentList.append(tempURL)

        print("Crawling Completed!\nTotal URLs:",
              visitedList.__len__(), "\nTotal Errors:", errorCount)
        return [articleURL, visitedList]

    def isArticle(self, url, soup):
        # Function determines if given url opens an news article
        articleURL = url
        article = False
        netloc = urlparse(url).netloc
        path = urlparse(url).path
        if netloc == 'www.ratopati.com':
            cond1 = re.match(r'/\d\d\d\d/\d\d/\d\d/\d\d\d\d\d\d.html', path) is not None
            div = soup.find('div', {'id': 'sing_cont'})
            cond2 = div is not None
            if (cond1 and cond2) is True:
                articleTitle = div.h2.text.encode('utf-8', 'ignore')
                articleDate = path.split('.')[0].split('/')[1:-1]
                articleURL = url
                article = True
        if netloc == 'www.setopati.com':
            pass
        else:
            pass

        if article is True:
            return [True, articleTitle, articleDate, articleURL]
        else:
            return [False]

    def multiCrawl(self, URL):
        # Each instance launched in different thread if craling multiple sites
        crawlURL = self.crawler(URL)

        for url in crawlURL[1]:
            if url not in self.URLs:
                self.URLs.append(url)

        for article in crawlURL[0]:
            if article not in self.Articles:
                self.Articles.append(article)

        self.sitesCrawled += 1

        self.storeURLs()

        print(self.URLs)
        print("Total URLs:", self.URLs.__len__())
        print(self.Articles)
        print("Total Articles:", self.Articles.__len__())
        print(self.sitesCrawled, "/",
              self.sourceURLs.__len__(), "Jobs Completed")

    def storeURLs(self):
        self.fileInUse.acquire()
        print("Writing to disk")
        urlList = []
        try:
            f = open('sites', 'rb')
            urlList = pickle.load(f)
            for url in self.URLs:
                if url not in urlList:
                    urlList.append(url)

            f.close()
            print("Loaded old database")
        except:
            urlList = self.URLs
            print("Error in database. Creating new database")

        f = open('sites', 'wb')
        pickle.dump(urlList, f, protocol=pickle.HIGHEST_PROTOCOL)
        f.close()

        print("Link stored successfully")
        self.fileInUse.release()

    def startCrawl(self):
        self.fileInUse = threading.Lock()
        for URL in self.sourceURLs:
            print("URL:", URL)
            threadName = urlparse(URL).netloc.split('@')[-1].split(':')[0]
            self.multiCrawl(URL)
            # newThread = threading.Thread(target=self.multiCrawl, args=(URL,), name = threadName)
            # newThread.start()
