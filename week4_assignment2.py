
# coding: utf-8

# Title: Week 4 assignment 2 - parsing HTML using BeautifulSoup
# Author: Meenakshi Parameshwaran
# Date: 31/03/16

# In this assignment you will write a Python program that expands on http://www.pythonlearn.com/code/urllinks.py. The program will use urllib to read the HTML from the data files below, extract the href= vaues from the anchor tags, scan for a tag that is in a particular position relative to the first name in the list, follow that link and repeat the process a number of times and report the last name you find.

# In[89]:

# %load urllinks.py - use this to load in a .py to .ipynb


# In[90]:

import urllib
from bs4 import BeautifulSoup


# In[91]:

url = input('Enter URL: ')
count = int(input('Enter count: '))
position = int(input('Enter position: '))


# In[92]:

myhtml = urllib.request.urlopen(url).read()
soup = BeautifulSoup(myhtml, "lxml")


# In[93]:

mytags = list()

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    # Look at the parts of a tag
    # print ('TAG:',tag) # keep this in, shows the full TAG
    # print (tag.get('href', None))
    mytags.append(tag.get('href', None))   


# In[94]:

for c in range(count):
    print(c+1)
    nexturl = mytags[position-1]
    print('Retrieving:', nexturl)
    nexthtml = urllib.request.urlopen(nexturl).read()
    soup = BeautifulSoup(nexthtml, "lxml")
    mytags = list()
    tags = soup('a')
    for tag in tags:
        # Look at the parts of a tag
        # print (tag.get('href', None))
        mytags.append(tag.get('href', None))

