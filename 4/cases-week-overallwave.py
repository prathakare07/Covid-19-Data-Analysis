#!/usr/bin/env python
# coding: utf-8

# In[5]:


import json 
import csv
import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[6]:


n=open('neighbor-districts-modified.json',)
data=json.load(n)
csv_file=pd.read_csv('cases-week-statewave.csv')
df=pd.DataFrame(csv_file,columns=['State_Name','Week_no','No_of_cases'])
state_list=df.State_Name
date_lst=df.Week_no.to_list()
cases_lst=df.No_of_cases


# In[7]:


week_wise={"Time_id":[],"No_of_cases":[],}
time_id_val=[]
no_of_cases_v=[]


# In[8]:


date_list=[]
for i in range(1,149):
    date_list.append(i)
print(len(date_list))


# In[9]:


state_lst=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']
state_values=[]
k=0
for i in range(len(state_lst)):
    state_values.append(k)
state_dict=dict(zip(state_lst,state_values))


# In[10]:


week=1
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
    time_id_val.append(week)
    week+=1
    no_of_cases_v.append(Sum)


# In[11]:





# In[12]:


week_wise["Time_id"]=time_id_val
week_wise["No_of_cases"]=no_of_cases_v


# In[13]:


final_frame=pd.DataFrame.from_dict(week_wise)
final_frame.to_csv(r'cases-overall-weekwise.csv',index=False)


# In[ ]:




