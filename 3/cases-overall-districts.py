#!/usr/bin/env python
# coding: utf-8

# In[6]:


import json 
import csv
import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[7]:


n=open('neighbor-districts-modified.json',)
data=json.load(n)
csv_file=pd.read_csv('districts (1).csv')
df=pd.DataFrame(csv_file,columns=['Date','District','Confirmed'])
dist_list=df.District.to_list()
date_lst=df.Date
cases_lst=df.Confirmed


# In[8]:


Overall={"districtid":[],"timeid":[],"cases":[],}
district_key_val=[]
time_id_val=[]
no_of_cases_v=[]


# In[9]:


end_date=date(2021,8,14)
start_date=date(2020,3,15)
date_list=[]
timestampStr='String'
day_count = (end_date - start_date).days + 1
for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
    date=single_date.strftime("%Y-%m-%d")
    if(date=="2021-08-14"):
            timestampStr = single_date.strftime("%Y-%m-%d")
            date_list.append(timestampStr)
            
date_values=[]
k=0
for i in range(len(date_list)):
    date_values.append(k)
date_dict=dict(zip(date_list,date_values))


# In[10]:


for i in data:
    idx=[j for j in range(len(dist_list)) if dist_list[j]==i[3:]]
    date_dict_1=date_dict
    
    for k in idx:
        if date_lst[k] in date_dict_1:
            date_dict_1[date_lst[k]]=cases_lst[k]
    time_id="Overall"
    prev=0
    lp=[]
    for j in date_dict_1:
        lp.append(date_dict_1[j])
        time_id_val.append(time_id)
        district_key_val.append(i)
        no_of_cases_v.append(abs(lp[0]))


# In[11]:





# In[12]:


Overall["districtid"]=district_key_val
Overall["timeid"]=time_id_val
Overall["cases"]=no_of_cases_v


# In[13]:


final_frame=pd.DataFrame.from_dict(Overall)
final_frame.sort_values(["districtid","timeid"]).to_csv(r'cases-Overall.csv',index=False)


# In[ ]:




