#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[5]:


num=pd.read_csv("cowin_vaccine_data_districtwise.csv")
df=pd.DataFrame(num,)
state_lst=df.State.to_list()


# In[7]:


df2=df.drop([0],axis=0)
df2.fillna(0)
state_list=df2.State.to_list()


# In[9]:





# In[10]:





# In[11]:


cols = df2.columns.drop('State')
df2[cols] = df2[cols].apply(pd.to_numeric, errors='coerce')


# In[12]:





# In[13]:


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
        timestampStr = single_date.strftime("%d/%m/%Y.3")
        date_list1.append(timestampStr)
        timestampSt  = single_date.strftime("%d/%m/%Y.4")
        date_list2.append(timestampSt)
k=0


# In[14]:


overall={"statename":[],"timeid":[],"dose1":[],"dose2":[],}
dist_key_val=[]
week_val=[]
dose1_val=[]
dose2_val=[]


# In[15]:


state_lst=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']
state_values=[]
k=0
for i in range(len(state_lst)):
    state_values.append(k)
state_dict=dict(zip(state_lst,state_values))


# In[16]:


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
    
    lp1=[]
    prev1=0
    week_no="Overall"
    for j in new1:
        lp1.append(j)
    for k in range(len(lp1)):
        dist_key_val.append(i)
        week_val.append(week_no)
        dose1_val.append(abs(lp1[k]-prev1))
        prev1=lp1[k]
    new2=[]
    for k in date_list2:
        new_2=[]
        col_list=df2[k].to_list()    
        for q in range(len(ind)):
            new_2.append(col_list[ind[q]])
        Sum=sum(new_2)
        new2.append(Sum)
    lp2=[]
    prev2=0
    for j in new2:
        lp2.append(j)
    for k in range(len(lp2)):
        dose2_val.append(abs(lp2[k]-prev2))
        prev2=lp2[k]


# In[17]:





# In[18]:


overall["statename"]=dist_key_val
overall["timeid"]=week_val
overall["dose1"]=dose1_val
overall["dose2"]=dose2_val


# In[19]:


final_frame=pd.DataFrame.from_dict(overall)
final_frame.sort_values("statename").to_csv(r'state-vaccinated-count-overall.csv',index=False)


# In[ ]:





# In[ ]:




