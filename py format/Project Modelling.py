#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np


# In[12]:


project = pd.read_csv("C:/Users/Dell/Desktop/Dataset for Modelling.csv",sep=",")
project.head()


# In[13]:


x = project.drop(["CompleteCustomerChurn","AccountName","AccountNumber"],axis=1)
y = project["CompleteCustomerChurn"]


# In[14]:


from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=.3,random_state=1)
from sklearn.linear_model import LogisticRegression
logmodel = LogisticRegression()
logmodel.fit(x_train,y_train)


# In[15]:


predictions = logmodel.predict(x_test)
predictions

from sklearn.metrics import classification_report
classification_report(y_test,predictions)
from sklearn.metrics import accuracy_score
accuracy_score(y_test,predictions)


# In[ ]:







# # Without split

# In[24]:


# preparing model considering all the variables 
# for regression model

import numpy as np
import statsmodels.formula.api as sm


# In[30]:


# Preparing model                  
ml = sm.logit('CompleteCustomerChurn~CustomerAgeCategoryIndicator+AcctPaymentStatusIndicator+RepChangesinLast002Months_SUM+NumberOfProductionInstances_SUM+OptyWonLast12Months_Percent_SUM+OverallEngagementSatisfactionIndicator_SUM+FulfillerPriceCategoryIndicator+KnowledgeEventAttendeeCount+TotalAdoptionPercent+LicensedAdoptionPercent+AdoptionCategoryIndicator+LicensingCategoryIndicator+ResponseRatePercent+NPSSatisfactionIndicator_SUM+OverallSupportSurveySatisfactionIndicator_SUM+UsageRiskIndicator_SUM+TotalActivityCount_SUM',data=project).fit() # regression model


# In[31]:


ml.params


# In[28]:


ml.summary()


# In[32]:


ml.pred_table()


# In[33]:


accuracy1 = (3341+101)/(3341+30+86+101)
accuracy1


# In[ ]:





# In[ ]:





# In[ ]:





# ### Removing parameters having greater P value

# #### Removing fuller price category indicator

# In[35]:


ml2= sm.logit('CompleteCustomerChurn~CustomerAgeCategoryIndicator+AcctPaymentStatusIndicator+RepChangesinLast002Months_SUM+NumberOfProductionInstances_SUM+OptyWonLast12Months_Percent_SUM+OverallEngagementSatisfactionIndicator_SUM+KnowledgeEventAttendeeCount+TotalAdoptionPercent+LicensedAdoptionPercent+AdoptionCategoryIndicator+LicensingCategoryIndicator+ResponseRatePercent+NPSSatisfactionIndicator_SUM+OverallSupportSurveySatisfactionIndicator_SUM+UsageRiskIndicator_SUM+TotalActivityCount_SUM',data=project).fit() 


# In[36]:


ml2.params


# In[37]:


ml2.summary()


# In[38]:


ml2.pred_table()


# In[39]:


accuracy2 = (3341+100)/(3341+30+87+100)
accuracy2


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Removing Licensed adoption percent

# In[40]:


ml3= sm.logit('CompleteCustomerChurn~CustomerAgeCategoryIndicator+AcctPaymentStatusIndicator+RepChangesinLast002Months_SUM+NumberOfProductionInstances_SUM+OptyWonLast12Months_Percent_SUM+OverallEngagementSatisfactionIndicator_SUM+KnowledgeEventAttendeeCount+TotalAdoptionPercent+AdoptionCategoryIndicator+LicensingCategoryIndicator+ResponseRatePercent+NPSSatisfactionIndicator_SUM+OverallSupportSurveySatisfactionIndicator_SUM+UsageRiskIndicator_SUM+TotalActivityCount_SUM',data=project).fit() 


# In[41]:


ml3.pred_table()


# In[46]:


accuracy3 = (3342+100)/(3342+29+87+100)
accuracy3


# In[ ]:





# In[ ]:





# In[ ]:





# ### Removing TotalActivityCount_SUM

# In[44]:


ml4= sm.logit('CompleteCustomerChurn~CustomerAgeCategoryIndicator+AcctPaymentStatusIndicator+RepChangesinLast002Months_SUM+NumberOfProductionInstances_SUM+OptyWonLast12Months_Percent_SUM+OverallEngagementSatisfactionIndicator_SUM+KnowledgeEventAttendeeCount+TotalAdoptionPercent+AdoptionCategoryIndicator+LicensingCategoryIndicator+ResponseRatePercent+NPSSatisfactionIndicator_SUM+OverallSupportSurveySatisfactionIndicator_SUM+UsageRiskIndicator_SUM',data=project).fit() 


# In[45]:


ml4.pred_table()


# In[47]:


accuracy4 = (3341+101)/(3341+30+86+101)
accuracy4


# In[ ]:




