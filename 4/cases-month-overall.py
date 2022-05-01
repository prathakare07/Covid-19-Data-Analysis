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
csv_file=pd.read_csv('cases-month-state.csv')
df=pd.DataFrame(csv_file,columns=['State_Name','Month_no','No_of_cases'])
state_list=df.State_Name
date_lst=df.Month_no.to_list()
cases_lst=df.No_of_cases


# In[3]:


month_wise={"Time_id":[],"No_of_cases":[],}
time_id_val=[]
no_of_cases_v=[]


# In[4]:


date_list=[]
for i in range(1,18):
    date_list.append(i)


# In[5]:


state_lst=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']
state_values=[]
k=0
for i in range(len(state_lst)):
    state_values.append(k)
state_dict=dict(zip(state_lst,state_values))


# In[6]:


month=1
for i in date_list:
    idx=[j for j in range(len(date_lst)) if date_lst[j]==i]
    state_dict_1=state_dict
    
    for k in idx:
        if state_list[k] in state_dict_1:
            state_dict_1[state_list[k]]=cases_lst[k]
    lp=[]
    for j in state_dict_1:
        lp.append(state_dict_1[j])
    Sum=sum(lp)
    time_id_val.append(month)
    month+=1
    no_of_cases_v.append(Sum)


# In[ ]:





# In[7]:


month_wise["Time_id"]=time_id_val
month_wise["No_of_cases"]=no_of_cases_v


# In[8]:


final_frame=pd.DataFrame.from_dict(month_wise)
final_frame.to_csv(r'cases-overall-month.csv',index=False)


# In[ ]:




