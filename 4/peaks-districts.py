#!/usr/bin/env python
# coding: utf-8

# In[11]:


import json 
import csv
import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[12]:


n=open('neighbor-districts-modified.json',)
data=json.load(n)
csv_file=pd.read_csv('cases-month-districts.csv')
df1=pd.DataFrame(csv_file,columns=['District_key','Month_no','No_of_cases'])
dist_list1=df1.District_key.to_list()
dist_monthlist=df1.Month_no
dist_monthcases=df1.No_of_cases
csv_file2=pd.read_csv('cases-week-districtswave.csv')
df2=pd.DataFrame(csv_file2,columns=['District_key','Week_no','No_of_cases'])
dist_list2=df2.District_key.to_list()
dist_weeklist=df2.Week_no
dist_weekcases=df2.No_of_cases


# In[13]:


week_wise={"districtid":[],"wave1-weekid":[],"wave2-weekid":[],"wave1-monthid":[],"wave2-monthid":[],}
district_key_val=[]
wave1_weekidval=[]
wave2_weekidval=[]
wave1_monthidval=[]
wave2_monthidval=[]


# In[14]:


for i in data:
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


# In[15]:


for i in data:
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


# In[16]:





# In[17]:


week_wise["districtid"]=district_key_val
week_wise["wave1-weekid"]=wave1_weekidval
week_wise["wave2-weekid"]=wave2_weekidval
week_wise["wave1-monthid"]=wave1_monthidval
week_wise["wave2-monthid"]=wave2_monthidval


# In[18]:


final_frame=pd.DataFrame.from_dict(week_wise)
final_frame.sort_values(["districtid"]).to_csv(r'district-peaks.csv',index=False)


# In[ ]:




