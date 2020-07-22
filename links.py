#!/usr/bin/env python3
#./links.py https://www.python.org/
import sys,re
from urllib.request import urlopen
from bs4 import BeautifulSoup
url = sys.argv[1]

response = urlopen(url)
content = response.read()
#text = content.decode('utf-8')

#https://pythonspot.com/extract-links-from-webpage-beautifulsoup/

soup = BeautifulSoup(content, 'html.parser')

for link in soup.findAll('a', attrs={'href': re.compile("^http://")}):
	print (link.get('href'))



