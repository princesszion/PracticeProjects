import requests
from bs4 import BeautifulSoup

page = requests.get(
    'https://www.amazon.com/best-sellers-books-Amazon/zgbs/books/ref=zg_bs_pg_1?_encoding=UTF8&pg=1')

soup = BeautifulSoup(page.content, 'html.parser')

links = soup.select(
    "#zg-ordered-list li span div span a > div")

first10 = links[:10]

for anchor in first10:
    print(anchor.text)