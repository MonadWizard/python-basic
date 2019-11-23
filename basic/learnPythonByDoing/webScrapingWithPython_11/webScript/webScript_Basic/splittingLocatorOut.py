# now we separate locator into classes

import re
from bs4 import BeautifulSoup

# html of online shopping site
ITEM_HTML = '''<html><head></head><body>
<li class = "col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
        <div class="image_container">
            <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad375348658385693.jpg" alt=A Light in the Attic" class="thumbnail"></a>

        </div>
        <p class="star-rating Three">
            <i class="icon-star"></i>
            <i class="icon-start"></i>
            <i class="icon-star"></i>
            <i class="icon-start"></i>
            <i class="icon-star"></i>
        </p>
        <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A light in the attic">A Light in the ...</a></h3>
        <div class="product_price">
    <p class="price_color">€51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>

        In stock

</p>

<form>
    <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to
</form>  
        </div>
    </article>
</li>     

</body></html>
'''


# locator for an item in the HTML page.
# This allow us to easily see what our code will be looking at as well as change it quickly if we notice it is now different
class ParsedItemLocator:
    NAME_LOCATOR = 'article.product_pod h3 a'
    LINK_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


# A class to take in an HTML page (or part of it), and find properties of an item it. make incapsulation
class ParsedItem:

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    # find title
    @property
    def name_h3(self):
        locator = ParsedItemLocator.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    # find link
    @property
    def link_h3(self):
        locator = ParsedItemLocator.LINK_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['href']
        return item_name

    # or find_price can work as
    @property
    def price(self):
        locator = ParsedItemLocator.PRICE_LOCATOR
        item_pricee = self.soup.select_one(locator).string
        return item_pricee

        # to extract $ we need to import re   to use regular expression
        pattern = '€([0-9]+\.[0-9]+)'  # if we have $ then make none type return error
        matcher = re.search(pattern, item_pricee)
        print(bool(matcher))
        print(matcher.group(0))
        print(matcher.group(1))
        return float(matcher.group(1))

    @property
    def rating(self):
        locator = ParsedItemLocator.RATING_LOCATOR
        star_rating_tag = self.soup.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        # rating_classes = filter(lambda x: x != 'star-rating', classes)
        return rating_classes


item = ParsedItem(ITEM_HTML)
print(item.name_h3)
