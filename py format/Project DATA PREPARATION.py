#!/usr/bin/env python
# coding: utf-8

# # Data preparation

# In[40]:


import pandas as pd


# In[41]:


c= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/ITSAAvgPrice.csv")
b = pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/UsageIndicator.csv")

merged = pd.merge(c,b,on='AccountNumber')
merged.to_csv("output.csv", index=False)


# In[42]:


print(merged.count())


# In[43]:


a = pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/AllCustomerChurnIndicator.csv",encoding="ISO-8859-1")
merged2=a.merge(b.merge(c,on='AccountNumber',how='inner'),on='AccountNumber',how='inner')


# In[44]:


merged2.head()


# In[ ]:





# In[ ]:





# ### left join

# In[45]:


c = pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/AllCustomerChurnIndicator.csv",encoding="ISO-8859-1")
merged2=a.merge(b.merge(c,on='AccountNumber',how='left'),on='AccountNumber',how='left')
merged2.head()


# In[ ]:





# In[ ]:





# In[46]:


c = pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/AllCustomerChurnIndicator.csv",encoding="ISO-8859-1")
merged3=a.merge(b.merge(c,on='AccountNumber',how='left'),on='AccountNumber',how='left')
merged3


# In[48]:


d=pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/AccountMetrics.csv",encoding="ISO-8859-1")
e=pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/CommunityMetrics.csv")
f=pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/EngagementSurveyMetrics.csv")
g=pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/KnowledgeEventMetrics.csv")
h=pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/LicensedAdoptionMetrics.csv",encoding="ISO-8859-1")
i=pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/NPSMetrics.csv",encoding="ISO-8859-1")
j=i=pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/SupportSurveyMetrics.csv",encoding="ISO-8859-1")


# In[49]:


FinalMerge1=a.merge(b.merge(c.merge(d.merge(e.merge(f.merge(g.merge(h.merge(i.merge(j,on='AccountNumber',how='left'),on='AccountNumber',how='left'),on='AccountNumber',how='left'),on='AccountNumber',how='left'),on='AccountNumber',how='left'),on='AccountNumber',how='left'),on='AccountNumber',how='left'),on='AccountNumber',how='left'),on='AccountNumber',how='left')


# In[50]:


FinalMerge1


# In[ ]:





# In[51]:


df=pd.DataFrame(FinalMerge1)
df.to_csv(r'C:/Users/Dell/Desktop/Datasets/Project/Merged/FinalMerge_metro.csv') 


# In[ ]:


df.drop('AcctName',axis=1)


# In[ ]:





# In[ ]:


FinalMerge = FinalMerge.drop(["AccountName_y","AcctName"],axis=1)


# In[ ]:


FinalMerge.head()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


FinalMerge


# ### final merge with inner

# In[36]:


FinalMerged=a.merge(b.merge(c.merge(d.merge(e.merge(f.merge(g.merge(h.merge(i.merge(j,on='AccountNumber',how='inner'),on='AccountNumber',how='inner'),on='AccountNumber',how='inner'),on='AccountNumber',how='inner'),on='AccountNumber',how='inner'),on='AccountNumber',how='inner'),on='AccountNumber',how='inner'),on='AccountNumber',how='inner'),on='AccountNumber',how='inner')


# In[ ]:





# In[37]:


FinalMerged


# In[ ]:


FinalMerge.head()


# In[ ]:


df=pd.DataFrame(FinalMerge)
df.to_csv(r'C:/Users/Dell/Desktop/Datasets/Project/Merged/FinalMerge.csv') 


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# ### Dropping on final merge

# In[19]:


Final= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/Merged/FinalMerge.csv")


# In[20]:


Final.head()


# In[22]:


Final = Final.drop(["CompleteCustomerChurn_y",],axis=1,inplace=True)


# In[23]:


Final.head(10)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Single single read

# In[52]:


a = pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/AllCustomerChurnIndicator.csv",encoding="ISO-8859-1")


# In[57]:


a


# In[53]:


b = pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/AccountMetrics.csv",encoding="ISO-8859-1")


# In[58]:


b


# In[55]:


merged1= pd.merge(a,b,on='AccountNumber',how='left')


# In[56]:


merged1


# In[59]:


c= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/AccountMetrics.csv",encoding="ISO-8859-1")
c


# In[61]:


merged2=pd.merge( pd.merge(a,b,on='AccountNumber',how='left'),c,on='AccountNumber',how='left')
merged2


# In[63]:


d= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/EngagementSurveyMetrics.csv",encoding="ISO-8859-1")
d


# In[65]:


merged3=pd.merge(pd.merge( pd.merge(a,b,on='AccountNumber',how='left'),c,on='AccountNumber',how='left'),d,on='AccountNumber',how='left')
merged3


# In[66]:


e= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/ITSAAvgPrice.csv",encoding="ISO-8859-1")
e


# In[68]:


merged4=pd.merge(pd.merge(pd.merge( pd.merge(a,b,on='AccountNumber',how='left'),c,on='AccountNumber',how='left'),d,on='AccountNumber',how='left'),e,on='AccountNumber',how='left')
merged4


# In[70]:


f= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/KnowledgeEventMetrics.csv",encoding="ISO-8859-1")
f


# In[71]:


merged5=pd.merge(pd.merge(pd.merge(pd.merge( pd.merge(a,b,on='AccountNumber',how='left'),c,on='AccountNumber',how='left'),d,on='AccountNumber',how='left'),e,on='AccountNumber',how='left'),f,on='AccountNumber',how='left')
merged5


# In[72]:


g= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/LicensedAdoptionMetrics.csv",encoding="ISO-8859-1")
g


# In[77]:


merged6=pd.merge(pd.merge(pd.merge(pd.merge(pd.merge( pd.merge(a,b,on='AccountNumber',how='left'),c,on='AccountNumber',how='left'),d,on='AccountNumber',how='left'),e,on='AccountNumber',how='left'),f,on='AccountNumber',how='left'),f,on='AccountNumber',how='left')
merged6


# In[78]:


h= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/NPSMetrics.csv",encoding="ISO-8859-1")
h


# In[80]:


merged7=pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge( pd.merge(a,b,on='AccountNumber',how='left'),c,on='AccountNumber',how='left'),d,on='AccountNumber',how='left'),e,on='AccountNumber',how='left'),f,on='AccountNumber',how='left'),f,on='AccountNumber',how='left'),h,on='AccountNumber',how='left')
merged7


# In[81]:


i= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/SupportSurveyMetrics.csv",encoding="ISO-8859-1")
i


# In[82]:


merged8=pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge( pd.merge(a,b,on='AccountNumber',how='left'),c,on='AccountNumber',how='left'),d,on='AccountNumber',how='left'),e,on='AccountNumber',how='left'),f,on='AccountNumber',how='left'),f,on='AccountNumber',how='left'),h,on='AccountNumber',how='left'),i,on='AccountNumber',how='left')
merged8


# In[83]:


j= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/UsageIndicator.csv",encoding="ISO-8859-1")
j


# In[85]:


merged9=pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge( pd.merge(a,b,on='AccountNumber',how='left'),c,on='AccountNumber',how='left'),d,on='AccountNumber',how='left'),e,on='AccountNumber',how='left'),f,on='AccountNumber',how='left'),f,on='AccountNumber',how='left'),h,on='AccountNumber',how='left'),i,on='AccountNumber',how='left'),j,on='AccountNumber',how='left')
merged9


# In[86]:


merged9.head()


# In[89]:


df=pd.DataFrame(merged9)
df.to_csv(r'C:/Users/Dell/Desktop/Datasets/Project/Merged/FinalMergeMetro.csv') 


# In[92]:


dataset= pd.read_csv("C:/Users/Dell/Desktop/Datasets/Project/Merged/FinalMergeMetro.csv",encoding="ISO-8859-1")


# In[93]:


dataset


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


df.to_csv(r'C:/Users/Dell/Desktop/Datasets/Project/Merged/FinalMergeMetro.csv') 

