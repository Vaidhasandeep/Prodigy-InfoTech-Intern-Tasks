#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings('ignore')


# In[9]:


df = pd.read_csv('C:\\Users\\v.omsai\\Downloads\\Metadata_Country_API_SP.POP.TOTL_DS2_en_csv_v2_392208.csv')
df.head()


# In[10]:


df.info()


# In[13]:


df['Region'].value_counts()


# In[14]:


df['IncomeGroup'].value_counts()


# In[22]:


region_income = df.groupby(['Region','IncomeGroup']).size().unstack(fill_value=0)
region_data = region_income.groupby('Region').sum()
region_data.plot(kind='bar')


# In[29]:


region_incomegroup = pd.crosstab(df['Region'],df['IncomeGroup'])
region_incomegroup


# In[32]:


df_heat = pd.DataFrame({
    x_label: grp['IncomeGroup'].value_counts()
    for x_label,grp in df.groupby('Region')
})
sns.heatmap(df_heat,cmap = 'viridis')


# In[50]:


group_count = df['Region'].value_counts()
plt.rcParams['figure.figsize'] = (20,10)
sns.barplot(x = group_count.index,y = group_count.values,palette = 'muted')
plt.xticks(rotation = 90)


for x,y in enumerate(group_count.values):
    plt.text(x,y,str(y), ha='center', va='bottom')


# In[51]:


df['Region'].value_counts().plot(kind='bar',color='skyblue')


# In[ ]:




