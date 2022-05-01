#!/usr/bin/env python
# coding: utf-8

# In[46]:


import json 
import csv
import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[47]:


n=open('neighbor-districts-modified.json',)
data=json.load(n)
csv_file=pd.read_csv('districts (1).csv')
df=pd.DataFrame(csv_file,columns=['Date','District','Confirmed'])
dist_list=df.District.to_list()
date_lst=df.Date
cases_lst=df.Confirmed


# In[48]:


month_wise={"District_key":[],"Month_no":[],"No_of_cases":[],}
district_key_val=[]
time_id_val=[]
no_of_cases_v=[]


# In[49]:


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


# In[50]:


for i in data:
    idx=[j for j in range(len(dist_list)) if dist_list[j]==i[3:]]
    date_dict_1=date_dict
    
    for k in idx:
        if date_lst[k] in date_dict_1:
            date_dict_1[date_lst[k]]=cases_lst[k]
    count=0
    month_no=1
    prev=0
    lp=[]
    for j in date_dict_1:
        lp.append(date_dict_1[j])
    for k in range(len(lp)):
        time_id_val.append(month_no)
        month_no+=1
        district_key_val.append(i)
        this=lp[k]
        if(k==0):
            no_of_cases_v.append(abs(lp[k]))
        else:
            no_of_cases_v.append(abs(lp[k]-prev))
        prev=this


# In[51]:





# In[52]:


month_wise["District_key"]=district_key_val
month_wise["Month_no"]=time_id_val
month_wise["No_of_cases"]=no_of_cases_v


# In[53]:


final_frame=pd.DataFrame.from_dict(month_wise)
final_frame.to_csv(r'cases-month-districts.csv',index=False)


# In[ ]:




