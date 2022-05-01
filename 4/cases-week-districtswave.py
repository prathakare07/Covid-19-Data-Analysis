#!/usr/bin/env python
# coding: utf-8

# In[112]:


import json 
import csv
import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[113]:


n=open('neighbor-districts-modified.json',)
data=json.load(n)
csv_file=pd.read_csv('districts (1).csv')
df=pd.DataFrame(csv_file,columns=['Date','District','Confirmed'])
dist_list=df.District.to_list()
date_lst=df.Date
cases_lst=df.Confirmed


# In[114]:


week_wise={"District_key":[],"Week_no":[],"No_of_cases":[],}
district_key_val=[]
time_id_val=[]
no_of_cases_v=[]


# In[115]:


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


# In[116]:


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


# In[117]:





# In[118]:


for i in data:
    idx=[j for j in range(len(dist_list)) if dist_list[j]==i[3:]]
    date_dict_1=date_dict1
    
    for k in idx:
        if date_lst[k] in date_dict_1:
            date_dict_1[date_lst[k]]=cases_lst[k]
    p=0
    week_no=1
    prev=0
    lp=[]
    for j in date_dict_1:
        lp.append(date_dict_1[j])
    for k in range(len(lp)):
        time_id_val.append(week_no)
        week_no+=2
        district_key_val.append(i)
        this=lp[k]
        if(k==0):
            no_of_cases_v.append(abs(lp[k]))
        else:
            no_of_cases_v.append(abs(lp[k]-prev))
        prev=this


# In[119]:





# In[120]:


week_wise["District_key"]=district_key_val
week_wise["Week_no"]=time_id_val
week_wise["No_of_cases"]=no_of_cases_v


# In[121]:


final_frame1=pd.DataFrame.from_dict(week_wise)


# In[125]:


week_wise={"District_key":[],"Week_no":[],"No_of_cases":[],}
district_key_val=[]
time_id_val=[]
no_of_cases_v=[]


# In[126]:


for i in data:
    idx=[j for j in range(len(dist_list)) if dist_list[j]==i[3:]]
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
        district_key_val.append(i)
        this=lp[k]
        if(k==0):
            no_of_cases_v.append(abs(lp[k]))
        else:
            no_of_cases_v.append(abs(lp[k]-prev))
        prev=this


# In[127]:





# In[128]:


week_wise["District_key"]=district_key_val
week_wise["Week_no"]=time_id_val
week_wise["No_of_cases"]=no_of_cases_v


# In[129]:


final_frame2=pd.DataFrame.from_dict(week_wise)


# In[131]:


frames=[final_frame1,final_frame2]
final_frame=pd.concat(frames)


# In[132]:





# In[133]:


final_frame.to_csv(r'cases-week-districtswave.csv',index=False)


# In[ ]:




