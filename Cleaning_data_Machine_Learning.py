#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv("covid_data_Machine_Learning_2.csv")


# In[3]:


df.head()


# In[4]:


## dropping unwanted columns 

df.drop(["Country_code", "WHO_region"], axis = 1, inplace=True)


# In[5]:


df.head()


# In[6]:


## checking for null values

df.isnull().sum()


# In[7]:


## checking for rows with 'Other' as country classified which was discovered during inspection of data

(df['Country'] == 'Other').sum()


# In[8]:


## dropping 'Other' countries

df.drop(df[df['Country']=='Other'].index, inplace = True)


# In[9]:


(df['Country'] == 'Other').sum()


# In[10]:


## creating an index column

index_column = [x for x in range(1,len(df)+1)]


# In[11]:


## inserting the index column

df.insert(0,'id',index_column)


# In[12]:


df.head()


# In[14]:


df.to_csv("covid_data_Machine_Learning_2.csv", index = False)


# In[ ]:




