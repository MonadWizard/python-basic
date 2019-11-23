import requests
from bs4 import BeautifulSoup


page = requests.get('http://www.example.com')
print(page.content)

print("""
""")

soup = BeautifulSoup(page.content, 'html.parser')

# get title h1
print(soup.find('h1').string)

# get link
print(soup.select_one('p a').attrs['href'])




