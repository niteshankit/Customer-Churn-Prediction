#!/usr/bin/env python
# coding: utf-8

# ## Data Analysis

# In[1]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[4]:


project = pd.read_csv("C:/Users/Dell/Desktop/FINALDATASET.csv",sep=",")
project.head()


# In[5]:


project.info()


# In[9]:


project.isnull().sum()


# In[10]:


sns.countplot(x="CompleteCustomerChurn",data=project)


# In[11]:


sns.heatmap(project.isnull(),yticklabels=False,cmap="viridis")


# In[13]:


sns.pairplot(project)


# In[14]:


sns.countplot(x="CompleteCustomerChurn",hue="CustomerAgeCategoryIndicator",data=project)


# In[15]:


sns.countplot(x="CompleteCustomerChurn",hue="AcctPaymentStatusIndicator",data=project)


# In[16]:


sns.countplot(x="CompleteCustomerChurn",hue="RepChangesinLast00.2Months_SUM",data=project)


# In[17]:


sns.countplot(x="CompleteCustomerChurn",hue="NumberOfProductionInstances_SUM",data=project)


# In[19]:


sns.countplot(x="CompleteCustomerChurn",hue="OverallEngagementSatisfactionIndicator_SUM",data=project)


# In[20]:


sns.countplot(x="CompleteCustomerChurn",hue="FulfillerPriceCategoryIndicator",data=project)


# In[21]:


sns.countplot(x="CompleteCustomerChurn",hue="AdoptionCategoryIndicator",data=project)


# In[22]:


sns.countplot(x="CompleteCustomerChurn",hue="LicensingCategoryIndicator",data=project)


# In[ ]:




