'''
Scraping Numbers from HTML using BeautifulSoup
In this assignment you will write a Python program
similar to https://www.py4e.com/code/urllinks.py.
The program will use urllib to read the HTML from the data files below,
and parse the data, extracting numbers and compute the
sum of the numbers in the file.

We provide two files for this assignment.
One is a sample file where we give you the sum for your testing and
the other is the actual data you need to process for the assignment.

Sample data: http://python-data.dr-chuck.net/comments_42.html (Sum=2553)
Actual data: http://python-data.dr-chuck.net/comments_353539.html (Sum ends with 63)
You do not need to save these files to your folder since your program
will read the data directly from the URL. Note: Each student will have a
distinct data url for the assignment - so only use your own data url for analysis.
'''
# Note - this code must run in Python 2.x and you must download
# http://www.pythonlearn.com/code/BeautifulSoup.py
# Into the same folder as this program

import urllib.request as urllib
from bs4 import *

url = input('Enter - ')
html = urllib.urlopen(url).read()
soup = BeautifulSoup(html,"html.parser")

# Retrieve all of the span tags
tags = soup('span')
sum = sum([int(tag.get_text()) for tag in tags])
#for tag in tags:
#    sum = sum + int(tag.get_text())
print(sum)
