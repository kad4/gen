import lxml
import pickle
import re
import sys
import threading
import urllib.request

from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin
from urllib.request import urlopen

def parser(URL):
	print ("Parsing:",URL)
	try:
		currentPage = urlopen(URL).read()
		soup = BeautifulSoup(currentPage)
		# print (currentPage)
		if soup.rss == None:
			parseHTML(URL, currentPage, soup)
		else:
			parseXML(URL, currentPage, soup)
	except Exception as e:
		print ('Error parsing',URL)
		print (e)

def parseHTML(URL, PAGE, SOUP):
	print ("Parsing HTML")
	try:
		currentPage = PAGE
		soup = SOUP

		titles = []
		
		for link in soup.find_all('a'):
			titles.append([link.string, link.get('href')])
			
		f = open('list.lst', 'wb')
		print ("written")
		pickle.dump(titles,f, protocol = pickle.HIGHEST_PROTOCOL)


	except Exception as e:
		print (e)
		raise
		
def parseXML(URL, PAGE, SOUP):
	print ("Parsing XML")
	try:
		currentPage = urlopen(URL).read()
		soup = BeautifulSoup(currentPage, 'xml')


	except Exception as e:
		print (e)
		raise
		
if __name__ == '__main__':
	parser('http://www.ekantipur.com/np/archive/')
