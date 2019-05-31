#!/usr/bin/env python
# coding: utf-8

# In[68]:


import pandas as pd
import numpy as np
location = "datasets/kickstartercombo (1).csv"
df = pd.read_csv(location)


# In[69]:


df.head()


# In[70]:


df.count()


# In[71]:


df['main_category'].value_counts()


# In[72]:


df.isnull().sum()


# In[73]:


df.sort_values('goal',ascending=True)


# In[74]:


df.sort_values('currency')


# In[75]:


df['currency'].value_counts()


# In[76]:


df.dropna()


# In[77]:


df.dropna(axis=1)


# In[91]:


df.sort_values(by='usd_goal_real'ascending=False)
df.sort_values(by='backers'ascending=False)
df.sort_values(by='state', ascending=False)


# In[112]:


df.sort_values(['main_category'])


# In[ ]:


df.drop_duplicates('failed',)


# In[ ]:





# df.sort_values('Main_category

# In[119]:


df['main_category'] = pd.Categorical(df['Music'])
df


# In[ ]:




