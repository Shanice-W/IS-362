#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np

path_to_html = 'https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/airports.csv'

df = pd.read_csv(path_to_html, index_col=0)

df2 = df.reset_index()

print(df2.head())


# In[3]:


df2.sort_values(by=['lon'], ascending=False).head()


# In[4]:


rowid_north = df2['lon'].idxmax()

north_name = df.iloc[rowid_north]['name']
north_lat = df.iloc[rowid_north]['lat']
north_lon = df.iloc[rowid_north]['lon']

print("The northern most airport is {}, located at {}° latitude and {}° longtitude.".format(north_name, north_lat, north_lon))


# In[5]:


df2.sort_values(by=['lat'], ascending=False).head()


# In[6]:


path_to_html = 'https://raw.githubusercontent.com/hadley/nycflights13/master/data-raw/weather.csv'

df3 = pd.read_csv(path_to_html, index_col=0)

df4 = df3.reset_index()

print(df4.head())


# In[7]:


feb12 = df4[(df4.month == 2) & (df4.day == 12) & (df4.year == 2013)].reset_index()

feb12.sort_values(by=['wind_speed'], ascending=False).head()


# In[8]:


feb12.drop([3], inplace = True)

feb12.reset_index(inplace = True)

feb12.sort_values(by=['wind_speed'], ascending=False).head()


# In[9]:


windiest = feb12['wind_speed'].idxmax()

origin = feb12.iloc[windiest]['origin']
speed = feb12.iloc[windiest]['wind_speed']

print("The windiest airport on February 12, 2013 was {}, with a wind speed of {} MPH.".format(origin, "{:,.2f}".format(round(speed,2))))

