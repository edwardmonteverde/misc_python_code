# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

#cd Desktop\Coursera\Python\Class 3

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/known_by_Fikret.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

urlnum = 0
count = 0
for tag in tags:
	while count < 3:
		if urlnum == 2:
			print(tag.contents[0])
			url2 = tag.get('href', None)
			html2 = urllib.request.urlopen(url, context=ctx).read()
			soup2 = BeautifulSoup(html, 'html.parser')
			urlnum = 0
			count = count + 1
		else:
			urlnum = urlnum + 1
		