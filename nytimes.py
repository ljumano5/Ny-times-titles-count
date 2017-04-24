import requests
import lxml
from lxml import html

r=requests.get('https://www.nytimes.com/')
pejd = lxml.html.fromstring(r.content)
naslovi = pejd.find_class('story-heading')
n=0
a=0
for el in naslovi:
    words = (el.text_content()).split()
    if 'Love' in words:
        a += 1

    n += 1
    print (el.text_content()).encode('ascii', 'replace')
print n
print a
