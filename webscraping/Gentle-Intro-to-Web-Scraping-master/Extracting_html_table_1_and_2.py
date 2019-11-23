#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import time


# In[3]:


url ='http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html'

headers= {'User-Agent': 'Mozilla/5.0'}


# In[4]:


response = requests.get(url)


# In[5]:


response.status_code


# In[6]:


response.content


# In[8]:


soup = BeautifulSoup(response.content, 'html.parser')


# In[9]:


stat_table =soup.find_all('table', class_ = 'MsoTableWeb3' )


# In[10]:


len(stat_table)


# In[11]:


stat_table = stat_table[0]


# In[24]:


for row in stat_table.find_all('tr'):
    for cell in row.find_all('td'):
        print(cell.text)
    


# In[25]:


with open ('disease.csv', 'w') as r:
    for row in stat_table.find_all('tr'):
        for cell in row.find_all('td'):
            r.write(cell.text.ljust(22))
        r.write('\n')
    


# In[ ]:


#http://www.whoishostingthis.com/tools/user-agent/


# In[ ]:


#'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'


# # video 2

# In[21]:


import requests
from bs4 import BeautifulSoup
import time


# In[3]:





# In[ ]:


#http://www.espn.com/nba/statistics/player/_/stat/assists/sort/avgAssists/count/41


# In[23]:


num = 1

url ='http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html'.format(num)

headers= {'User-Agent': 'Mozilla/5.0'}
with open ('basketball_stats.txt', 'w') as r:
    r.write('BASKETBALL ASSISTS TABLE\n')


while num < 500:
    url ='http://people.dbmi.columbia.edu/~friedma/Projects/DiseaseSymptomKB/index.html'.format(num)
    
    time.sleep(1)
    response = requests.get(url, headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        stat_table = soup.find_all('table', class_ = 'MsoTableWeb3')
        if len(stat_table) < 2:
            stat_table = stat_table[0]
            with open ('basketball_stats.txt', 'a') as r:
                for row in stat_table.find_all('tr'):
                    for cell in row.find_all('td'):
                        r.write(cell.text.ljust(22))
                    r.write('\n')
        else: print('Too many tables')
    
    else:
        print('No response')
        print(num)
        
    
    num += 40
                
                
    
    


# In[ ]:





# In[ ]:




