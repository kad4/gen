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
			parseHTML(URL)
		else:
			parseXML(URL)
	except Exception as e:
		print ('Error parsing',URL)
		print (e)

def parseHTML(URL):
	try:
		currentPage = urlopen(URL).read()
		soup = BeautifulSoup(currentPage)

		newItem = soup.findAll("div", id = True)
		print (newItem)

	except Exception as e:
		print (e)
		
def parseXML(URL):
	try:
		currentPage = urlopen(URL).read()
		soup = BeautifulSoup(currentPage, 'xml')
	except Exception as e:
		print (e)
		
if __name__ == '__main__':
	parser('http://localhost/genSites/sites/b0news.htm')
