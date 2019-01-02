#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import warnings
warnings.filterwarnings('ignore')
data = pd.read_csv('BreadBasket_DMS.csv')
sns.set_palette('husl',1,0.75)


# In[2]:


data.info()


# In[3]:


print('\n', 'Number of Transactions done per month', '\n')

data['Date time']= pd.to_datetime(data['Date']+' '+data['Time'])
data['Year and Month']=data['Date time'].map(lambda x: 100*x.year + x.month)
Transaction_by_month=data[['Year and Month','Transaction']].groupby('Year and Month',as_index=False).sum()

plt.figure(figsize=[10,5])
sns.barplot(x='Year and Month',y='Transaction',data=Transaction_by_month)
plt.ticklabel_format(style='plain', axis='y')
plt.title('Number of Transactions per month')
sns.set_style("darkgrid")
sns.set_palette('husl',1,0.75)


# In[4]:


print('\n', 'Number of Transactions done per day', '\n')

data['Days']=data['Date time'].dt.weekday_name

plt.figure(figsize=[10,5])
sns.boxplot(x='Days',y='Transaction',data=data)
plt.ticklabel_format(style='plain', axis='y')
plt.title('Number of Transactions per Day')
sns.set_style("darkgrid")
sns.set_palette('husl',1,0.75)


# In[5]:


print('\n', 'Number of times the top 10 Items sold', '\n')

most_sold = data['Item'].value_counts().head(10)
print('\n', most_sold, '\n')

print('\n', 'Top 10 Items sold', '\n')

plt.subplot(1,1,1)
most_sold.plot(kind='bar')
plt.title('Top 10 Most Number of Items Sold')
sns.set_style("darkgrid")
sns.set_palette('husl',1,0.75)


# In[6]:


print('\n', 'Number of Unique Items in a dataset : ', data['Item'].nunique())
print( '\n', data['Item'].unique(), '\n')

