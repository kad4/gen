import pickle
import re
import sys
import threading
import urllib.request

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen
	
allUrls = ['http://www.ratopati.com/']
'''[
	'https://www.ratopati.com/',
	'http://www.bbc.co.uk/nepali/news/',
	'http://www.ekantipur.com/np/',
	'http://www.onlinekhabar.com/',
	'http://www.setopati.com/',
]'''

sitesCrawled = 0
killProcess = False
opener = urllib.request.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')]
urllib.request.install_opener(opener)

def crawler(URL):
	currentList = [URL]
	visitedList = [URL]

	parsedURL = urlparse(URL)
	print ("Crawling",parsedURL.netloc)

	errorCount = 0
	while currentList.__len__() > 0:
		# print (currentList.__len__())
		url = currentList.pop(0)
		print ("Current URL:",url[0:100])

		try:
			currentPage = urlopen(url).read()
			print (currentPage)
			soup = BeautifulSoup(currentPage)
		except Exception as e:
			print ('Error loading', url[0:100])
			print (e)
			errorCount += 1
			continue

		if url not in visitedList:
			visitedList.append(url)

		soupLinks = soup.findAll("a", href = True)
		for soupLink in soupLinks:
			
			tempURL = urljoin(url, soupLink['href'])
			
			if URL not in tempURL:
				continue

			reTempURL = re.findall(r'(.*)#.*', tempURL)

			if reTempURL != []:
				tempURL = reTempURL[0]

			if tempURL not in visitedList and tempURL not in currentList:
				currentList.append(tempURL)
			
			if killProcess==True:
				currentList.clear()


	print ("Crawling Completed!\nTotal URLs:", visitedList.__len__(), "\nTotal Errors:", errorCount)
	return visitedList

def multiCrawl(URL):
	global sitesCrawled, URLs

	crawlURL = crawler(URL)

	for url in crawlURL:
		URLs.append(url)

	sitesCrawled += 1
	storeURLs()

	print (sitesCrawled,"/",allUrls.__len__(), "Jobs Completed")

def storeURLs():
	global fileInUse, URLs

	fileInUse.acquire()
	print ("Writing to disk")
	urlList = []
	try:
		f = open('sites', 'rb')
		urlList = pickle.load(f)
		for url in URLs:
			if url not in urlList:
				urlList.append(url)

		f.close()
		print ("Loaded old database")
	except:
		urlList = URLs
		print ("Error in database. Creating new database")

	f = open('sites', 'wb')
	pickle.dump(urlList,f, protocol = pickle.HIGHEST_PROTOCOL)
	f.close()

	print ("Link stored successfully")
	fileInUse.release()

if __name__ == '__main__':
	global fileInUse

	fileInUse = threading.Lock()

	URLs = []
	Threads = []
	
	for URL in allUrls:
		threadName = urlparse(URL).netloc.split('@')[-1].split(':')[0]
		newThread = threading.Thread(target = multiCrawl, args = (URL,), name = threadName)
		Threads.append(newThread)
		newThread.start()

	while(threading.active_count() > 1):
		if (sys.stdin.read(1) == 's'):
			killProcess = True





			
