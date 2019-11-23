import requests
from bs4 import BeautifulSoup
import time


url ='http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html'
headers= {'User-Agent': 'Mozilla/5.0'}


response = requests.get(url)
response.status_code

response.content


soup = BeautifulSoup(response.content, 'html.parser')

stat_table =soup.find_all('table', class_ = 'MsoTableWeb3' )

len(stat_table)

stat_table = stat_table[0]


for row in stat_table.find_all('tr'):
    for cell in row.find_all('td'):
        print(cell.text)

'''
with open ('disease.csv', 'w') as r:
    for row in stat_table.find_all('tr'):
        for cell in row.find_all('td'):
            r.write(cell.text.ljust(22))
        r.write('\n')
'''    


with open ('diseases.csv', 'w') as r:
    for row in stat_table.find_all('tr'):
        r.write(cell.text.ljust(222222))
        r.write('\n')












