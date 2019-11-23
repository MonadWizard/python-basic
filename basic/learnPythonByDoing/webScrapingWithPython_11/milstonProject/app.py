import requests
from pages.all_books_page import AllBooksPage

page_content = requests.get('http://books.toscrape.com').content
page = AllBooksPage(page_content)

books = page.books

"""
for book in books:
    print(book)
"""

# for multi page
#http://books.toscrape.com/catalogue/category/books_1/page-4.html
for page_num in range(1, page.page_count):
    url = f'http://books.toscrape.com/catalogue/category/books_1/page-{page_num+1}.html'
    page_content = requests.get(url).content
    page = AllBooksPage(page_content)
    books.extend(page.books)
