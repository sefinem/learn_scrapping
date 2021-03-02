"""
Goal :
  To find 'next button' in the page. And give a signal that next page whether
  it's there or not so the program either stop or run

 
"""

import requests 
from bs4 import BeautifulSoup as BS

page = 1
URL = f'http://books.toscrape.com/catalogue/page-{page}.html'

def search_next(page):
  r = requests.get(URL)

  soup = BS(r.content, 'html5lib')
  return soup.find('li', attrs={'class': 'next'})

while search_next is not None and page < 6:
  search_next(page)
  print(f'Page {page}')
  page += 1









