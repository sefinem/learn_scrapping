"""
Goal:
  To find all info about the book on the display. In the end we store what we scrapped from the web
  to csv file.

Try to improve:
  - rating is not easily scrapped
  - if the filename we specified was there, instead overwritten the data will be added. So we want our data 
    be overwritten for now as we just scrapped for first page.
  - if we want to add the data we just scrapped, that means we want to scrape through all pages available.
    So there are over 50 pages we are going to scrappe

"""

import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://books.toscrape.com/'

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'html5lib')

frames = soup.findAll('article', attrs={'class':'product_pod'})

all_data = [['no','img_link','book_link','title','price','stock_availability']]
id = 0
for frame in frames:
  image_link = URL+frame.img['src']
  book_page_link = URL+frame.a['href']
  book_title = frame.h3.a['title']
  product_price = frame.find('p', class_='price_color').text
  stock_availability = frame.find('p', class_='instock').text.strip()
  all_data.append([id,image_link,book_page_link,book_title,product_price,stock_availability])
  id += 1

with open('book_list.csv','w', newline='') as file:
  writer = csv.writer(file)
  writer.writerows(all_data)
