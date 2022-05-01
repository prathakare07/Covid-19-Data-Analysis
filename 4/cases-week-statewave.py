#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json 
import csv
import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[2]:


csv_file=pd.read_csv('districts (1).csv')
df=pd.DataFrame(csv_file,columns=['Date','State','Confirmed'])
state_list=df.State.to_list()
date_lst=df.Date
cases_lst=df.Confirmed


# In[3]:


week_wise={"State_Name":[],"Week_no":[],"No_of_cases":[],}
state_val=[]
time_id_val=[]
no_of_cases_v=[]


# In[4]:


end_date=date(2021,8,15)
start_date=date(2020,3,22)
date_list=[]
timestampStr='String'
count=0
day_count = (end_date - start_date).days + 1
for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
    timestampStr = single_date.strftime("%Y-%m-%d")
    if(count%7==0):
        date_list.append(timestampStr)
    count+=1
date_values=[]
k=0
for i in range(len(date_list)):
    date_values.append(k)
date_dict1=dict(zip(date_list,date_values))


# In[5]:


end_date=date(2021,8,19)
start_date=date(2020,3,25)
date_list=[]
timestampStr='String'
count=0
day_count = (end_date - start_date).days + 1
for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
    timestampStr = single_date.strftime("%Y-%m-%d")
    if(count%7==0):
        date_list.append(timestampStr)
    count+=1
date_values=[]
k=0
for i in range(len(date_list)):
    date_values.append(k)
date_dict2=dict(zip(date_list,date_values))


# In[6]:


state_dict=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']


# In[7]:


for i in state_dict:
    idx=[j for j in range(len(state_list)) if state_list[j]==i]
    date_dict_1=date_dict1
    for p in date_dict_1:
        date_dict_1[p]=0
    for k in idx:
        if date_lst[k] in date_dict_1:
            date_dict_1[date_lst[k]]+=cases_lst[k]
    p=0
    week_no=1
    prev=0
    lp=[]
    for j in date_dict_1:
        lp.append(date_dict_1[j])
    for k in range(len(lp)):
        time_id_val.append(week_no)
        week_no+=2
        state_val.append(i)
        this=lp[k]
        if(k==0):
            no_of_cases_v.append(abs(lp[k]))
        else:
            no_of_cases_v.append(abs(lp[k]-prev))
        prev=this


# In[8]:





# In[9]:


week_wise["State_Name"]=state_val
week_wise["Week_no"]=time_id_val
week_wise["No_of_cases"]=no_of_cases_v


# In[10]:


final_frame1=pd.DataFrame.from_dict(week_wise)


# In[11]:


week_wise={"State_Name":[],"Week_no":[],"No_of_cases":[],}
state_val=[]
time_id_val=[]
no_of_cases_v=[]


# In[12]:


for i in state_dict:
    idx=[j for j in range(len(state_list)) if state_list[j]==i]
    date_dict_1=date_dict2
    
    for k in idx:
        if date_lst[k] in date_dict_1:
            date_dict_1[date_lst[k]]=cases_lst[k]
    p=0
    week_no=2
    prev=0
    lp=[]
    for j in date_dict_1:
        lp.append(date_dict_1[j])
    for k in range(len(lp)):
        time_id_val.append(week_no)
        week_no+=2
        state_val.append(i)
        this=lp[k]
        if(k==0):
            no_of_cases_v.append(abs(lp[k]))
        else:
            no_of_cases_v.append(abs(lp[k]-prev))
        prev=this


# In[13]:





# In[14]:


week_wise["State_Name"]=state_val
week_wise["Week_no"]=time_id_val
week_wise["No_of_cases"]=no_of_cases_v


# In[15]:


final_frame2=pd.DataFrame.from_dict(week_wise)


# In[16]:


frames=[final_frame1,final_frame2]
final_frame=pd.concat(frames)


# In[17]:


print(len(final_frame))


# In[18]:


final_frame.to_csv(r'cases-week-statewave.csv',index=False)


# In[ ]:




