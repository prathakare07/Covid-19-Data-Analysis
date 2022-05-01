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


csv_file=pd.read_csv('cases-month-state.csv')
df1=pd.DataFrame(csv_file,columns=['State_Name','Month_no','No_of_cases'])
dist_list1=df1.State_Name.to_list()
dist_monthlist=df1.Month_no
dist_monthcases=df1.No_of_cases
csv_file2=pd.read_csv('cases-week-statewave.csv')
df2=pd.DataFrame(csv_file2,columns=['State_Name','Week_no','No_of_cases'])
dist_list2=df2.State_Name.to_list()
dist_weeklist=df2.Week_no
dist_weekcases=df2.No_of_cases


# In[3]:


state_dict=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']


# In[4]:


week_wise={"statename":[],"wave1-weekid":[],"wave2-weekid":[],"wave1-monthid":[],"wave2-monthid":[],}
district_key_val=[]
wave1_weekidval=[]
wave2_weekidval=[]
wave1_monthidval=[]
wave2_monthidval=[]


# In[5]:


for i in state_dict:
    idx=[j for j in range(len(dist_list2)) if dist_list2[j]==i]
    wave1=[]
    wave2=[]
    for k in idx:
        if dist_weeklist[k]<91:
            wave1.append(dist_weekcases[k])
        else:
            wave2.append(dist_weekcases[k])
    max_val=max(wave1)
    max_val2=max(wave2)
    for m in idx:
        if dist_weekcases[m]==max_val and dist_weeklist[m]<91 :
            wave1week=dist_weeklist[m]
        if dist_weekcases[m]==max_val2 and dist_weeklist[m]>90:
            wave2week=dist_weeklist[m]
    wave1_weekidval.append(wave1week)
    wave2_weekidval.append(wave2week)
    district_key_val.append(i)


# In[6]:


for i in state_dict:
    idx=[j for j in range(len(dist_list1)) if dist_list1[j]==i]
    wave1_mnth=[]
    wave2_mnth=[]
    for k in idx:
        if dist_monthlist[k]<11:
            wave1_mnth.append(dist_monthcases[k])
        else:
            wave2_mnth.append(dist_monthcases[k])
    max_val=max(wave1_mnth)
    max_val2=max(wave2_mnth)
    for m in idx:
        if dist_monthcases[m]==max_val and dist_monthlist[m]<11 :
            wave1mnth=dist_monthlist[m]
        if dist_monthcases[m]==max_val2 and dist_monthlist[m]>10:
            wave2mnth=dist_monthlist[m]
    wave1_monthidval.append(wave1mnth)
    wave2_monthidval.append(wave2mnth)


# In[7]:





# In[8]:


week_wise["statename"]=district_key_val
week_wise["wave1-weekid"]=wave1_weekidval
week_wise["wave2-weekid"]=wave2_weekidval
week_wise["wave1-monthid"]=wave1_monthidval
week_wise["wave2-monthid"]=wave2_monthidval


# In[9]:


final_frame=pd.DataFrame.from_dict(week_wise)
final_frame.sort_values(["statename"]).to_csv(r'state-peaks.csv',index=False)


# In[ ]:




