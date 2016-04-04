
# coding: utf-8

# ## Title: Extracting Data from JSON
# ### Author: Meenakshi Parameshwaran
# ### Date: 04/04/16
# 
# Note that this assigment was written in Python 3.

# In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py. The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
# We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.
# 
# Sample data: http://python-data.dr-chuck.net/comments_42.json (Sum=2553)
# 
# Actual data: http://python-data.dr-chuck.net/comments_168486.json (Sum ends with 32)
# 
# You do not need to save these files to your folder since your program will read the data directly from the URL.
# 
# **Data Format**
# 
# The data consists of a number of names and comment counts in JSON as follows:
# 
# `{
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }`
# 
# The closest sample code that shows how to parse JSON and extract a list is json2.py. You might also want to look at geoxml.py to see how to prompt for a URL and retrieve data from a URL.
# 
# 
# **Sample Execution**
# 
# `
# $ python solution.py 
# Enter location: http://python-data.dr-chuck.net/comments_42.json
# Retrieving http://python-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2482
# `

# In[109]:

import urllib.request
import json


# In[110]:

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    url = address
    print ('Retrieving', url)
    
    uh = urllib.request.urlopen(url)
    
    # need to decode it for Python 3
    data = uh.readall().decode('utf-8')
    print ('Retrieved',len(data),'characters')

    try: 
        mycomments = json.loads(data)
    except:
        mycomments = None
    
#     print(type(mycomments))

#     print(json.dumps(mycomments, indent = 4))

#     print(mycomments.keys())
#     print(mycomments['comments'][0]['name'])
#     print(mycomments['comments'][0]['count'])

    mycounts = list()
    
    # need to subscript the comments key of the dictionary
    for item in mycomments['comments']:
        mycounts.append(item['count']) # then select the count list element of the comments dictionary

    print('Count of comments:', len(mycounts)) 
    print('Sum:', sum(mycounts))

