from bs4 import BeautifulSoup

from locators.quote_page_locators import QuotesPageLocators
from parsers.quote import QuoteParser


class QuotesPage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')  # initial bs4 for search contant

    @property
    def quotes(self):
        locator = QuotesPageLocators.QUOTE  # find a locator
        quote_tags = self.soup.select(locator)  # select every quote
        return [QuoteParser(e) for e in quote_tags]  # found tags but not string, that's bs4 tags
