#pip install requests - 1
#pip install lxml - 4
#pip install htmlparser - 5
#pip install selectolax - 6
#pip install beautifulsoup4 - 7

import requests #2
import re #3

import lxml.html
from selectolax.parser import HTMLParser
from bs4 import BeautifulSoup

import timeit

# 8
def extractLinksRegEx(txt):
    tgs = re.compile(r'<a[^<>]+?href=([\'\"])(.*?)\1', re.IGNORECASE)
    return [match[1] for match in tgs.findall(txt)]

#13
def extractLinksLxml(txt):
    lst = []
    dom = lxml.html.fromstring(txt)
    for l in dom.xpath('//a/@href'):
        lst.append(l)
    return lst

#15 
def extractLinksHtmlParser(txt):
    lst = []
    dom = HTMLParser(txt)
    for tag in dom.tags('a'):
        attrs = tag.attributes
        if 'href' in attrs:
            lst.append(attrs['href'])
    return lst

#17 
def extractBs(txt):
    lst = []
    s = BeautifulSoup(txt, 'lxml')
    for tag in s.find_all('a', href=True):
        lst.append(tag['href'])
    return lst

# 11
def printList(lst):
    for l in lst:
        print('Level 1 -> ' + l)

#21
def printListWithFltr(lst, fltr):
    for l in lst:
        if inFilter(l, fltr): 
            print('Level 1 -> ' + l)

# 21
def inFilter(l, fltr):
    r = False
    for f in fltr:
        if f in l:
            r = True
            break
    return r

#23
def followList(lst, fltr, prt=False):
    for l in lst:
        if inFilter(l, fltr): 
            print('Level 1 -> ' + l)
            if prt == False:
                r = requests.get(l)
                res = extractBs(r.text)
                for r in res:
                    print('Level 2 -> ' + r)

#9 
r = requests.get('https://edfreitas.me/')
#10
print(extractLinksRegEx(r.text))

#12
printList(extractLinksRegEx(r.text))

#14
printList(extractLinksLxml(r.text))

#16
printList(extractLinksHtmlParser(r.text))

#18
printList(extractBs(r.text))

#22
printListWithFltr(extractBs(r.text), ['pluralsight'])

#24
followList(extractBs(r.text), ['pluralsight'], False)

#20
tcode = '''
def extractBs(txt):
    lst = []
    s = BeautifulSoup(txt, 'lxml')
    for tag in s.find_all('a', href=True):
        lst.append(tag['href'])
    return lst
'''

#19
tsetup = "from bs4 import BeautifulSoup"
print(timeit.timeit(setup = tsetup, 
                    stmt = tcode, 
                    number = 10000))