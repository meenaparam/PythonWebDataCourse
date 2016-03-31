
# coding: utf-8

# In[36]:

## Title: Week 4 assignment 1 - parsing HTML using BeautifulSoup
## Author: Meenakshi Parameshwaran
## 31/03/16

# %load week4_assignment1.py - use this to load in a .py to .ipynb


# In[37]:

import urllib
from bs4 import BeautifulSoup


# In[38]:

url = input('Enter - ')


# In[39]:

myhtml = urllib.request.urlopen(url).read()
soup = BeautifulSoup(myhtml, "lxml")


# In[40]:

mycomments = list()

# Retrieve all of the span tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print ('TAG:',tag) # keep this in, shows the full TAG
    print ('CLASS:',tag.get('class', None))
    print ('Comments:',tag.contents[0])
    print ('Attrs:',tag.attrs)
    mycomments.append(tag.contents[0])
    


# In[41]:

print(mycomments)


# In[42]:

# convert the list mycomments into integers
mycomments_int = list(map(int, mycomments))


# In[43]:

print("Count:", len(mycomments_int))
print("Sum:", sum(mycomments_int))

