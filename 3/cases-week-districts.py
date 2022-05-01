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


n=open('neighbor-districts-modified.json',)
data=json.load(n)
csv_file=pd.read_csv('districts (1).csv')
df=pd.DataFrame(csv_file,columns=['Date','District','Confirmed'])
dist_list=df.District.to_list()
date_lst=df.Date
cases_lst=df.Confirmed


# In[4]:


week_wise={"districtid":[],"weekno":[],"cases":[],}
district_key_val=[]
time_id_val=[]
no_of_cases_v=[]


# In[5]:


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


# In[6]:


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
        week_no+=1
        district_key_val.append(i)
        this=lp[k]
        if(k==0):
            no_of_cases_v.append(abs(lp[k]))
        else:
            no_of_cases_v.append(abs(lp[k]-prev))
        prev=this


# In[8]:





# In[9]:


week_wise["districtid"]=district_key_val
week_wise["weekno"]=time_id_val
week_wise["cases"]=no_of_cases_v


# In[11]:


final_frame=pd.DataFrame.from_dict(week_wise)
final_frame.sort_values(["districtid","weekno"]).to_csv(r'cases-week.csv',index=False)


# In[ ]:




