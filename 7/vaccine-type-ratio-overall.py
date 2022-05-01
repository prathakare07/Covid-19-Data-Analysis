#!/usr/bin/env python
# coding: utf-8

# In[45]:


import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[46]:


num=pd.read_csv("cowin_vaccine_data_districtwise.csv")
df=pd.DataFrame(num,)
state_lst=df.State.to_list()


# In[47]:


df2=df.drop([0],axis=0)
df2.fillna(0)
state_list=df2.State.to_list()


# In[48]:





# In[49]:





# In[50]:


cols = df2.columns.drop('State')
df2[cols] = df2[cols].apply(pd.to_numeric, errors='coerce')


# In[51]:





# In[52]:


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


# In[62]:


overall={"region":[],"vaccineratio":[],}
dist_key_val=[]
vaccineratio_val=[]


# In[63]:


state_lst=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']
state_values=[]
k=0
for i in range(len(state_lst)):
    state_values.append(k)
state_dict=dict(zip(state_lst,state_values))


# In[64]:


lp1=[]
lp2=[]
for i in state_dict:
    ind=[]
    for j in range(len(state_list)):
        if (i==state_list[j]):
            ind.append(j)
    new1=[]
    for k in date_list1:
        new_1=[]
        col_list=df2[k].to_list()    
        for q in range(len(ind)):
            new_1.append(col_list[ind[q]])
        Sum=sum(new_1)
        new1.append(Sum)
    
    for j in new1:
        lp1.append(j)
    new2=[]
    for k in date_list2:
        new_2=[]
        col_list=df2[k].to_list()    
        for q in range(len(ind)):
            new_2.append(col_list[ind[q]])
        Sum=sum(new_2)
        new2.append(Sum)
    for j in new2:
        lp2.append(j)
dist_key_val.append("Overall")
Sumlp1=sum(lp1)
Sumlp2=sum(lp2)
vaccineratio_val.append(Sumlp2/Sumlp1)


# In[65]:





# In[66]:





# In[67]:


overall["region"]=dist_key_val
overall["vaccineratio"]=vaccineratio_val


# In[68]:


final_frame=pd.DataFrame.from_dict(overall)
final_frame.sort_values(["vaccineratio"]).to_csv(r'overall-vaccine-type-ratio.csv',index=False)


# In[ ]:




