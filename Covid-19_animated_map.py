#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Импортируем библиотеки 
import numpy as np
import pandas as pd 
import plotly as py
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)


# In[2]:


# Считываем данные
# Данные можно скачать по этой ссылке или же указать её: https://www.kaggle.com/sudalairajkumar/novel-corona-virus-2019-dataset
df = pd.read_csv("covid_19_data.csv", encoding='utf-8')


# In[3]:


# Форматирование названия колонок
df = df.rename(columns={'Country/Region': 'Country' , 'ObservationDate': 'Date'})


# In[4]:


# группировка по странам и дете и устранение повторов
df_countries = df.groupby(['Country', 'Date']).sum().reset_index().sort_values('Date', ascending=False)
df_countries = df_countries.drop_duplicates(subset = ['Country'])
df_countries = df_countries[df_countries['Confirmed'] > 0]


# In[5]:


# Задание параметров для визуализации
fig = go.Figure(data=go.Choropleth(
    locations = df_countries['Country'],
    locationmode = 'country names',
    z = df_countries['Confirmed'],
    colorscale = 'Reds',
    marker_line_color = 'black',
    marker_line_width = 0.4))

fig.update_layout(
    title_text = 'Подтвержденные случаи на 28 марта 2020',
    title_x = 0.4,
    geo=dict(
        showframe = False,
        showcoastlines = False,
        projection_type = 'equirectangular'))


# In[6]:


df_countrydate = df[df['Confirmed'] > 0]

df_countrydate.groupby(['Date','Country']).sum().reset_index()
df_countrydate

# Создание визуализации
fig = px.choropleth(df_countrydate, 
                    locations="Country", 
                    locationmode = "country names",
                    color="Confirmed", 
                    hover_name="Country", 
                    animation_frame="Date"
                   )
fig.update_layout(
    title_text = 'Global Spread of Coronavirus',
    title_x = 0.5,
    geo=dict(
        showframe = False,
        showcoastlines = False,
    ))
    
fig.show()


# In[ ]:




