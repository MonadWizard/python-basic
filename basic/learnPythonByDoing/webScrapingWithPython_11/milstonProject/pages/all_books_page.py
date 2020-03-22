from bs4 import BeautifulSoup
from locators.all_books_page import ALLBooksPageLocators
from parsers.book_parser import BookParser


class AllBooksPage:
    def __init__(self, page_content):  # built beautifulsoup object
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(ALLBooksPageLocators.BOOKS)]

    @property
    def page_count(self):
        content = self.soup.select_one(ALLBooksPageLocators.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9]+)'
