#!/usr/bin/env python
# coding: utf-8

#  Weather Dataset Analysis by KODI VENU

# In[1]:


import pandas as pd
import numpy as np


# In[3]:


data = pd.read_csv("weatherHistory.csv")


# In[5]:


data


# Analyzing the DataFrames

# .head() ---> First N rows of the data

# In[7]:


data.head()


# .shape() ---> Total no.of rows and columns of the dataset

# In[9]:


data.shape


# .index() ---> Index of the dataframe

# In[13]:


data.index


# .columns ---> Shows names of each column

# In[17]:


data.columns


# .dtypes ---> Shows the datatypes of each column

# In[19]:


data.dtypes


# .unique ---> In columns, it shows the unique values. It can be applied on a single column only

# In[23]:


data['Daily Summary'].unique()


# .nunique() ---> It shows total no.of unique values on a single column or whole dataframe

# In[25]:


data.nunique()


# .count() ---> It shows total no.of non-null values in each column, applied on single column or whole dataframe

# In[27]:


data.count()


# .value_counts ---> Shows all the unique values with their count and applied on single column only

# In[29]:


data['Daily Summary'].value_counts()


# .info() ---> Provides basic information about the dataframe

# In[31]:


data.info()


# Finding all the unique "Wind Speed" values in the data

# In[33]:


data.head(2)


# In[35]:


data.nunique()


# In[39]:


data['Wind Speed (km/h)'].nunique()


# In[41]:


data['Wind Speed (km/h)'].unique()


# Finding the number of times when the "Weather is exactly clear"

# In[43]:


data.head(2)


# In[45]:


# using value counts
data.Summary.value_counts()


# In[51]:


# using Filtering
data.head(2)
data.Summary == 'Clear'
data[data.Summary == 'Clear']


# In[53]:


# groupby
data.head(2)


# In[55]:


data.groupby('Summary').get_group('Clear')


# Finding the number of times when the "Wind Speed was exactly 4km/h"

# In[57]:


data.head(2)


# In[63]:


data[data['Wind Speed (km/h)'] == 4]


# Find out all the null values in the data

# In[66]:


data.isnull()


# In[68]:


data.isnull().sum()


# In[70]:


data.notnull().sum()


# Rename the column name 'Summary' to 'Weathrer Condition' 

# In[72]:


data.head(2)


# In[76]:


#For temporary purposes
data.rename(columns = {'Summary':'Weather Condition'})


# In[78]:


#For Permanent purpose
data.rename(columns = {'Summary':'Weather Condition'}, inplace=True)


# In[80]:


data.head(1)


# What is the mean 'Visibility'?

# In[82]:


data.head(1)


# In[84]:


data['Visibility (km)'].mean()


# In[106]:


pd.Series.str


# In[114]:


data.Visibility_km.mean()


# What is the Standard Deviation of 'Pressure' in this data?

# In[116]:


data.head(1)


# In[118]:


data['Pressure (millibars)'].std()


# In[120]:


data.Pressure (millibars).std()


# What is the Variance of 'Humidity' in this data?

# In[122]:


data.head(1)


# In[124]:


data.Humidity.var()


# In[126]:


#if space in column names, we use [] else we use . methods
data['Humidity'].var()


# Find out all the instances when the 'Snow' was recorded

# In[128]:


# using value_counts
#data.head(1)
data['Weather Condition'].value_counts()


# In[134]:


#Filtering
data[data['Weather Condition'] == 'Snow']


# In[138]:


#str.contains
data[data['Weather Condition'].str.contains('Snow')]


# Find out all the instances when 'Wind Speed is above 24' and 'Visibility is 25'

# In[140]:


data[(data['Wind Speed (km/h)'] > 24) & (data['Visibility (km)'] == 25)]


# What is the Mean value of each column against each 'Weather Condition'?

# In[167]:


#error due to non conversion of columns from obj into int or float type
data.groupby('Weather Condition').mean()


# What is the Minimum and Maximum value of each column against each 'Weather Condition'

# In[148]:


data.head(1)


# In[150]:


data.groupby('Weather Condition').min()


# In[152]:


data.groupby('Weather Condition').max()


# Show all the Records where the Weather Condition is 'Fog'

# In[158]:


data[data['Weather Condition'] == 'Fog']


# Find all the instances when 'Weather is Clear' or 'Visibility is above 40'

# In[160]:


data[(data['Weather Condition'] == 'Clear') | (data['Visibility (km)'] > 40)]


# Find all the instances when :
# 'Weather is Clear' and 'Humidity is greater than 50' or 'Visibility is above 40'

# In[162]:


data.head(1)


# In[164]:


data[(data['Weather Condition'] == 'Clear') & (data['Humidity'] > 50) | (data['Visibility (km)'] > 40)]


# In[ ]:




