#!/usr/bin/env python
# coding: utf-8

# In[16]:


import json 
import csv
import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[17]:


n=open('neighbor-districts-modified.json',)
data=json.load(n)
csv_file=pd.read_csv('districts (1).csv')
df=pd.DataFrame(csv_file,columns=['Date','State','Confirmed'])
state_list=df.State.to_list()
date_lst=df.Date
cases_lst=df.Confirmed


# In[18]:


month_wise={"State_Name":[],"Month_no":[],"No_of_cases":[],}
state_val=[]
time_id_val=[]
no_of_cases_v=[]


# In[19]:


end_date=date(2021,8,14)
start_date=date(2020,3,15)
date_list=[]
timestampStr='String'
day_count = (end_date - start_date).days + 1
for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
    date=single_date.strftime("%d")
    if(date=="14"):
            timestampStr = single_date.strftime("%Y-%m-%d")
            date_list.append(timestampStr)
date_values=[]
k=0
for i in range(len(date_list)):
    date_values.append(k)
date_dict=dict(zip(date_list,date_values))


# In[20]:


state_dict=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']


# In[21]:


for i in state_dict:
    idx=[j for j in range(len(state_list)) if state_list[j]==i]
    date_dict_1=date_dict
    for p in date_dict_1:
        date_dict_1[p]=0
    for k in idx:
        if date_lst[k] in date_dict_1:
            date_dict_1[date_lst[k]]+=cases_lst[k]
            
    count=0
    month_no=1
    prev=0
    lp=[]
    for j in date_dict_1:
        lp.append(date_dict_1[j])
    for k in range(len(lp)):
        time_id_val.append(month_no)
        month_no+=1
        state_val.append(i)
        this=lp[k]
        if(k==0):
            no_of_cases_v.append(abs(lp[k]))
        else:
            no_of_cases_v.append(abs(lp[k]-prev))
        prev=this


# In[22]:





# In[23]:


month_wise["State_Name"]=state_val
month_wise["Month_no"]=time_id_val
month_wise["No_of_cases"]=no_of_cases_v


# In[24]:


final_frame=pd.DataFrame.from_dict(month_wise)
final_frame.to_csv(r'cases-month-state.csv',index=False)


# In[ ]:




