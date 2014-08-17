import re

from urllib.parse import urlparse
from bs4 import BeautifulSoup

print(urlparse('https://w3.facebook.co.uk/').netloc.split('.'))

print('hello'.split('e')[-1], 'hello'.split('m'))

print(urlparse('http://www.facebook.com/').netloc)
print(urlparse('http://facebook.com').netloc)

f = open('try.htm', 'r')
list = f.read()
f.close()
soup = BeautifulSoup(list)
print(soup.findAll('p')[3].parent)
list = ['a', 'e', 3, 'o', 'u']
list.remove('e')
print(list)
