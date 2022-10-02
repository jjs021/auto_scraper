#!/usr/bin/env python
# coding: utf-8

# In[133]:


import requests
r = requests.get('https://www.newyorkfed.org/research')


# In[134]:


# print the first 500 characters of the HTML
print(r.text[0:100])


# In[135]:


from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')


# In[136]:


results = soup.find_all(attrs={"class":("ts-story-headline","ts-story-text")})
#Yay!


# In[66]:


len(results)


# In[67]:


results[0:4]


# In[98]:


first_result = results[0:2]


# In[99]:


first_result


# In[100]:


import pandas as pd


# In[101]:


first_result[0].find('a').text


# In[102]:


first_result[1].find('a').text


# In[103]:


first_result[0].find('a')['href']


# In[113]:


records = []
count=0

while count < len(results):
    result = results[count: count+2]
    count = count+2
    title = result[0].find('a').text
    summary = result[1].find('a').text
    url = result[0].find('a')['href']
    records.append((title, summary, url))


# In[114]:


records
##👍


# In[122]:


df = pd.DataFrame(records, columns=['title', 'summary', 'url'])


# In[128]:


df.head(10)


# In[129]:


df['summary'] = df['summary'].replace(r'\s+|\\n', ' ', regex=True) 
#Very useful!


# In[130]:


df.tail()


# In[131]:


df.shape


# In[132]:


df.to_csv('FED_research.csv', index=False)


# In[ ]:




