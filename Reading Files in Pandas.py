#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[3]:


df = pd.read_csv(r"C:\Users\bindu\Documents\DA\Python\Pandas\countries of the world.csv")
df


# In[7]:


#df1 = pd.read_csv(r"C:\Users\bindu\Documents\DA\Python\Pandas\countries of the world.txt", sep = '\t')
#df1

df1 = pd.read_table(r"C:\Users\bindu\Documents\DA\Python\Pandas\countries of the world.txt")
df1


# In[8]:


df1 = pd.read_json(r"C:\Users\bindu\Documents\DA\Python\Pandas\json_sample.json")
df1


# In[10]:


df1 = pd.read_excel(r"C:\Users\bindu\Documents\DA\Python\Pandas\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')
df1


# In[11]:


#To view all the rows
pd.set_option('display.max.rows', 235)


# In[19]:


df2 = pd.read_excel(r"C:\Users\bindu\Documents\DA\Python\Pandas\world_population_excel_workbook.xlsx", sheet_name = 'Sheet1')
df2


# In[13]:


#To view all the rows
pd.set_option('display.max.columns', 40)


# In[18]:


df1 = pd.read_json(r"C:\Users\bindu\Documents\DA\Python\Pandas\json_sample.json")
df1


# In[17]:


df2.info()


# In[20]:


df2.info()


# In[21]:


df2.shape


# In[22]:


df2.head(10)


# In[23]:


df2.tail(10)


# In[24]:


df2['Rank']


# In[25]:


df2.loc[224]


# In[26]:


df2.iloc[224]


# In[ ]:




