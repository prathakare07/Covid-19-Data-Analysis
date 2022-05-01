#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from datetime import date,timedelta
import datetime


# In[2]:


num=pd.read_csv("cowin_vaccine_data_districtwise.csv")
df=pd.DataFrame(num,)
dist_code_lst=df.District_Key.to_list()


# In[3]:


df2=df.drop([0],axis=0)
df2.fillna(0)
dist_code=df2.District_Key.to_list()


# In[ ]:





# In[ ]:





# In[4]:


cols = df2.columns.drop('District_Key')
df2[cols] = df2[cols].apply(pd.to_numeric, errors='coerce')


# In[5]:


end_date=date(2021,8,14)
start_date=date(2021,1,16)
date_list1=[]
date_list2=[]
timestampStr='String'
count=0
day_count = (end_date - start_date).days + 1
for single_date in [d for d in (start_date + timedelta(n) for n in range(day_count)) if d <= end_date]:
    if (count%7==0):
        timestampStr = single_date.strftime("%d/%m/%Y.3")
        date_list1.append(timestampStr)
        timestampSt  = single_date.strftime("%d/%m/%Y.4")
        date_list2.append(timestampSt)
    count=count+1
k=0


# In[6]:


week_wise={"districtid":[],"timeid":[],"dose1":[],"dose2":[],}
dist_key_val=[]
week_val=[]
dose1_val=[]
dose2_val=[]


# In[7]:


for i in dist_code:
    ind=dist_code.index(i)
    new1=[]
    for k in date_list1:
        col_list=df2[k].to_list()
        new1.append(col_list[ind])
    lp1=[]
    prev1=0
    week_no=1
    for j in new1:
        lp1.append(j)
    for k in range(len(lp1)):
        dist_key_val.append(i)
        week_val.append(week_no)
        week_no=week_no+1
        dose1_val.append(abs(lp1[k]-prev1))
        prev1=lp1[k]
    new2=[]
    for k in date_list2:
        col_list2=df2[k].to_list()
        new2.append(col_list2[ind])
    lp2=[]
    prev2=0
    for j in new2:
        lp2.append(j)
    for k in range(len(lp2)):
        dose2_val.append(abs(lp2[k]-prev2))
        prev2=lp2[k]


# In[ ]:





# In[8]:


week_wise["districtid"]=dist_key_val
week_wise["timeid"]=week_val
week_wise["dose1"]=dose1_val
week_wise["dose2"]=dose2_val


# In[9]:


final_frame=pd.DataFrame.from_dict(week_wise)
final_frame.sort_values(["districtid","timeid"]).to_csv(r'district-vaccinated-count-week.csv',index=False)


# In[ ]:



