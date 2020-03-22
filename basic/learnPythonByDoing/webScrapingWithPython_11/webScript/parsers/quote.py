from locators.quote_locators import QuoteLocators


class QuoteParser:
    # Given one of the specific quote divs, find out the data about the quote (quote content, author, tags).

    def __init__(self, parent):  # define div by parent
        self.parent = parent

    def __repr__(self):  # REPR METHOD TO PRINT OUT NICELY
        return f'<Quote {self.content}, by {self.author}>'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [e.string for e in self.parent.select(locator)]  # select all indevusal tags
