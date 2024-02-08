#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import plotly.express as px


# In[4]:


import plotly.graph_objects as go


# In[6]:


data=pd.read_csv("Screentime-App-Details.csv")


# In[8]:


data.head()


# In[9]:


data.describe()


# In[10]:


figure=px.bar(data_frame=data,x="Date",y="Usage",color="App",title="Usage")
figure.show()


# In[11]:


figure=px.bar(data_frame=data,x="Date",y="Notifications",color="App",title="Notifications")
figure.show()


# In[12]:


figure=px.bar(data_frame=data,x="Date",y="Times opened",color="App",title="Times opened")
figure.show()


# In[16]:


figure=px.scatter(data_frame=data,x="Notifications",y="Usage",size="Notifications",trendline="ols"
                  ,title="Relationship between number of notifications and usage")
figure.show()


# In[ ]:




