
# coding: utf-8

# In[54]:


import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.oabrj.org.br/")
c = r.content

c


# In[55]:


soup=BeautifulSoup(c,"html.parser")


# In[66]:


all=soup.find_all("div",{"class":""})


# In[67]:


all


# In[69]:


import pandas as pd

df= pd.DataFrame(all)
df.to_dict()

df


# In[70]:


df.to_csv('all.csv', index=False)
print('Done')


# In[73]:


df.head(5)


# In[74]:


import psycopg2

conn = psycopg2.connect("host=localhost dbname=diario_oficial user=postgres")
cur = conn.cursor()
cur.execute('''CREATE TABLE dados (
                id INT, 
                name TEXT
            )''')

conn.commit()
conn.close()


# In[76]:


import psycopg2

conn = psycopg2.connect("host=localhost dbname=diario_oficial user=postgres")
cur = conn.cursor()
with open('all.csv', 'r') as f:
    next(f)
    cur.copy_from(f, 'dados', sep=',')
    
conn.commit()

