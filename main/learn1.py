"""
Goal :
  The goal was to learn the process of web scrapping using python and beautifulsoup.

"""


# 1. Accessing the HTML content from webpage with requests module
# 2. Parsing the HTML content using BeautifulSoup
# 3. Searching and navigating through the parse tree

import requests
from bs4 import BeautifulSoup

URL = "http://books.toscrape.com/"
r = requests.get(URL)

# bucket to store books name
books = []

soup = BeautifulSoup(r.content, 'html5lib')
books = soup.find('ol')

for book in books.findAll('h3'):
  name = book.a['title']
  books.append(name)
  print(name);print()

print(len(books))











