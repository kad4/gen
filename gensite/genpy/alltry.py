import re

from urllib.parse import urlparse

print (urlparse('https://w3.facebook.co.uk/').netloc.split('.'))
