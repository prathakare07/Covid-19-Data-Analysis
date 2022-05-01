#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[2]:


num=pd.read_csv("cowin_vaccine_data_districtwise.csv")
df=pd.DataFrame(num,)
dist_code_lst=df.District_Key.to_list()


# In[3]:


df2=df.drop([0],axis=0)
df2.fillna(0)
dist_code=df2.District_Key.to_list()


# In[4]:





# In[5]:





# In[6]:


cols = df2.columns.drop('District_Key')
df2[cols] = df2[cols].apply(pd.to_numeric, errors='coerce')


# In[7]:





# In[8]:


end_date=date(2021,8,14)
start_date=date(2021,1,16)
date_list1=[]
date_list2=[]
timestampStr='String'
count=0
day_count = (end_date - start_date).days + 1
for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
    date=single_date.strftime("%d/%m/%Y")
    if(date=='14/08/2021'):
        timestampStr = single_date.strftime("%d/%m/%Y.8")
        date_list1.append(timestampStr)
        timestampSt  = single_date.strftime("%d/%m/%Y.9")
        date_list2.append(timestampSt)
k=0


# In[39]:


overall={"districtid":[],"vaccineratio":[],}
dist_key_val=[]
vaccineratio_val=[]


# In[40]:


for i in dist_code:
    ind=dist_code.index(i)
    new1=[]
    for k in date_list1:
        col_list=df2[k].to_list()
        new1.append(col_list[ind])
    lp1=[]
    prev1=0
    for j in new1:
        lp1.append(j)
    dist_key_val.append(i)
    new2=[]
    for k in date_list2:
        col_list2=df2[k].to_list()
        new2.append(col_list2[ind])
    lp2=[]
    for j in new2:
        lp2.append(j)
    if lp1[0]==0:
        vaccineratio_val.append(np.nan)
    else:
        vaccineratio_val.append(lp2[0]/lp1[0])


# In[41]:





# In[42]:


overall["districtid"]=dist_key_val
overall["vaccineratio"]=vaccineratio_val


# In[43]:


final_frame=pd.DataFrame.from_dict(overall)
final_frame.sort_values(["vaccineratio"]).to_csv(r'district-vaccine-type-ratio.csv',index=False)


# In[ ]:




