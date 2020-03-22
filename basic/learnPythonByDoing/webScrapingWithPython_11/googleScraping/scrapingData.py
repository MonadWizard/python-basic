import requests
from bs4 import BeautifulSoup

# page = requests.get('', headers={'User-Agent': 'mozilla/17.0'})
# print(page.content)
'''
url = 'https://www.google.com/search?q=president+of+bangladesh'
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
headers = {'User-Agent': user_agent}
response = requests.get(url,headers=headers)
html = response.content
print(response.content)



soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
'''

headers = {'User-Agent': 'Mozilla/5.0'}

url = "https://www.google.com/search?q=president+of+bangladesh"

r = requests.get(url, headers=headers)
print(r.text)

soup = BeautifulSoup(r.text, 'html.parser')
print(soup.prettify())
