"""
Goal:
Scrapping book's name in particular number of pages and end the process if there is no 'next button'
or specified number of page (In the future we wanna end the process if there isn't next button)

Description:
The book's name that we scrapped are stored in a list and in the end of the program we can see
how many books had just been scrapped

"""


import requests
from bs4 import BeautifulSoup

page = 1
books = []

def find_book_name(page):
  temp_books = []

  URL = f'http://books.toscrape.com/catalogue/page-{page}.html'
  r = requests.get(URL)
  soup = BeautifulSoup(r.content, 'html5lib')
  books = soup.find('ol')

  for book in books.findAll('h3'):
    name = book.a['title']
    temp_books.append(name)
  
  next_button = soup.find('li', attrs={'class': 'next'})

  return temp_books, next_button

books_of_page = ''
while books_of_page is not None and page < 6:
  print(f'Now we\'re scrapping page {page}')
  books_of_page, next_button = find_book_name(page)
  books += books_of_page
  page += 1

print(f'All books are {len(books)}')
print()