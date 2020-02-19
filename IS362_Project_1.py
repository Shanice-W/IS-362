#!/usr/bin/env python
# coding: utf-8

# In[10]:


import pandas as pd
import numpy as np

path_to_file = open("C:\\Users\shani\Downloads\Project_1.csv")

airlines = pd.read_csv(path_to_file)

print(airlines)


# In[12]:


airlines = airlines.drop(airlines[airlines.status == 'on time'].index)

airlines2 = airlines.sort_values(by = ['number_of_flights'], ascending=False)


# In[13]:


airlines2[airlines2.name == 'AM WEST']


# In[14]:


airlines2[airlines2.name == 'ALASKA']


# In[15]:


airlines3 = airlines2.drop(labels = ['name', 'status'], axis=1)


# In[16]:


group = airlines3.groupby(['destination']).agg('sum').sort_values(by = ['number_of_flights'], ascending=False).reset_index()

print(group)


# In[17]:


print("The Top Three Cities With the Greatest Delays: ")

top_three = group.head(3)


for row in range(len(top_three)):
    print(top_three.iloc[row]['destination'])

