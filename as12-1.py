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

url = "http://py4e-data.dr-chuck.net/comments_141652.html"
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('span')

for tag in tags:
		# Look at the parts of a tag
		print ('TAG:',tag)
		print ('URL:',tag.get('href', None))
		print ('Contents:',tag.contents[0])
		print ('Attrs:',tag.attrs)
"""
total = 0
for i in tags:
	num = int(i.contents[0])
	total = total + num

print(total)
"""