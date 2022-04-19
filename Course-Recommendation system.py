#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[3]:


courses=pd.read_csv('udemy_courses.csv')
appendix=pd.read_csv('appendix.csv')


# In[4]:


courses.head(1)


# In[5]:


appendix.head(1)


# In[37]:


courses.merge(appendix,on='course_title').shape


# In[7]:


courses=courses[['course_id','course_title','url','is_paid','price','num_subscribers','num_reviews','subject']]


# In[8]:


appendix['Course Number'].value_counts()


# In[9]:


courses['course_id'].value_counts()


# In[10]:


courses.info()


# In[11]:


courses.isnull().sum()


# In[19]:


courses.drop_duplicates(subset=None, keep='first', inplace=False)


# In[38]:


courses.duplicated().sum()


# In[29]:


duplicateRows = courses [courses.duplicated()] 
print(duplicateRows)


# In[46]:


courses.drop_duplicates(inplace=True)
courses.duplicated().sum()


# In[47]:


duplicateRows = courses [courses.duplicated()] 
print(duplicateRows)


# In[48]:


courses.iloc[0].subject


# In[49]:


courses.head()


# In[1]:


courses['course_title'][0]


# In[ ]:




