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

soup = BeautifulSoup(ITEM_HTML, 'html.parser')


# find title
def find_item_name_h3():
    locator = 'article.product_pod h3 a'
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['title']
    print(item_name)


find_item_name_h3()
print("""
""")


# find link
def find_link_h3():
    locator = 'article.product_pod h3 a'
    item_link = soup.select_one(locator)
    item_name = item_link.attrs['href']
    print(item_name)


find_link_h3()
print("""
""")


def find_price():
    paragraph = soup.find('p', {'class': 'price_color'})
    # print(paragraph)
    print(paragraph.string)


find_price()
print("""
""")


# or find_price can work as
def find_item_price():
    locator = 'article.product_pod p.price_color'
    item_pricee = soup.select_one(locator).string
    print(item_pricee)

    # to extract $ we need to import re   to use regular expression
    pattern = '€([0-9]+\.[0-9]+)'
    matcher = re.search(pattern, item_pricee)
    print(bool(matcher))
    print(matcher.group(0))
    print(matcher.group(1))
    print(float(matcher.group(1)))


find_item_price()
print("""
""")


def find_item_rating():
    locator = 'article.product_pod p.star-rating'
    star_rating_tag = soup.select_one(locator)
    classes = star_rating_tag.attrs['class']
    rating_classes = [r for r in classes if r != 'star-rating']
    # rating_classes = filter(lambda x: x != 'star-rating', classes)
    print(rating_classes)


find_item_rating()
print("""
""")


