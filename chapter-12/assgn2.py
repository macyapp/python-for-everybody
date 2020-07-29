from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Data Scraping
tags = soup('span')
sm = 0
cn = 0
for tag in tags:
    cn += 1
    sm += int(tag.contents[0])

print('Count %d' % cn)
print('Sum %d' % sm)