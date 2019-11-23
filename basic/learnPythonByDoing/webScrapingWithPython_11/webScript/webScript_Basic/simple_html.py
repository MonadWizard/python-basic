from bs4 import BeautifulSoup

SIMLE_HTML = """
<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class='subtitle'>Lorem ip sum dolor sit a met. Consectetur edipiscim jwerhternd jg fjhwsaoij.</p>
<p>here's another p without a class </p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>

</ul>
</body>
</html>
"""
simple_soup = BeautifulSoup(SIMLE_HTML, 'html.parser')

print(simple_soup.find('h1'))
print(simple_soup.find('h1').string)


# or with a function
def find_title():
    h1_tag = simple_soup.find('h1')
    print(h1_tag.string)


find_title()
print("""
""")


# find list item
def find_list_items():
    list_item = simple_soup.find_all('li')
    list_contents = [e.string for e in list_item]  # list comprehention
    print(list_item)
    print(list_contents)


find_list_items()
print("""
""")


def find_all_paragraph():
    paragraph = simple_soup.find('p', {'class': 'subtitle'})
    print(paragraph)
    print(paragraph.string)
    paragraph_all = simple_soup.find_all('p')
    print(paragraph_all)
    paragraph_contents = [p.string for p in paragraph_all]  # list comprehention
    print(paragraph_contents)


find_all_paragraph()
print("""
""")


# bautifulsoup can't find any paragraph which haven't any class. so we find all then remove class paragraph to find
# paragraph whitout class
def find_another_paragraph():
    paragraph_all = simple_soup.find_all('p')
    another_paragraph = [p for p in paragraph_all if 'subtitle' not in p.attrs.get('class', [])]    # we find class as dictionary so we need obj.attrs.get('class', [])
    print(another_paragraph)


find_another_paragraph()
print("""
""")
