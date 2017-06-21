# Add the link to the list
# Go Through the entire list
#       Is it KB? If so, then we are done
#   Else
#       Call open page func
#           This function will open the item on the list in question
#           it will then get all the links on that page
#           then add those links to the list
#   End (repeat process)

from BeautifulSoup import BeautifulSoup
import urllib2
import re
from urlparse import urlparse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
#from urllib.parse import urlparse

# Add first link to the list
#firstLink = "https://en.wikipedia.org/wiki/Drake_(musician)"
firstLink = 'https://en.wikipedia.org/wiki/Lori_Singer'


allLinks = []

allLinks.append(firstLink)

def getOnlyWiki(u):
    cleanList = []
    if u.startswith('http'):
        cleanList.append(u)
    return cleanList


def getLinks(url):
    # Get the links
    html_page = urllib2.urlopen(url)
    soup = BeautifulSoup(html_page)
    linksNew = []
    newList = soup.findAll('div', attrs={'class': 'mw-parser-output'})
    for link in newList:
        listTemp = link.findAll('a', href=True) #attrs={'href': re.compile("^http://")}):
        for a in listTemp:
            linksNew.append(a['href'])
    return linksNew


def printList(bodylist):
    for y in bodylist:
        print(y)

def printNum(bodylist):
    listCounter = 0
    for y in bodylist:
        listCounter = listCounter + 1
    return  listCounter

allLinks = getLinks(firstLink)

counter = 0

#printList(allLinks)

# Loop through the entire list

whileLink = firstLink

while (whileLink == firstLink):

    for x in allLinks:

        counter = counter + 1

        if x == "/wiki/Kevin_Bacon":
            print("You Win!")
            whileLink = x
            break
        else:
            if allLinks[counter].startswith('/wiki'):
            # get all links from the page in question
                currentLink = 'https://en.wikipedia.org' + allLinks[counter]
                linksToAdd = getLinks(currentLink)
               # print('NillaPleaseNewSection')
                allLinks = allLinks + linksToAdd


print(printNum(allLinks))