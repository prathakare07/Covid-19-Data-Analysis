#!/usr/bin/env python
# coding: utf-8

# In[68]:


import json
import csv
import pandas as pd
import numpy as np
from pandas import ExcelFile
import datetime


# In[69]:


num=pd.read_csv("cowin_vaccine_data_districtwise.csv")
df=pd.DataFrame(num,columns=["State","07/08/2021.3","14/08/2021.3"])
dist_code_lst=df.State.to_list()


num2= pd.read_excel("Census Data.xlsx")
df2=pd.DataFrame(num2,columns=["Level","Name","TRU","TOT_P"])
Dist_Name=df2.Name.to_list()
tru=df2.TRU.to_list()
total=df2.TOT_P.to_list()
lvl=df2.Level.to_list()


# In[70]:


df1=df.drop([0],axis=0)
cols = df1.columns.drop('State')
df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')
state_code=df1.State.to_list()


# In[71]:


state_lst=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']
state_values=[]
k=0
for i in range(len(state_lst)):
    state_values.append(k)
state_dict=dict(zip(state_lst,state_values))


# In[72]:


state_wise={"stateid":[],"populationleft":[],"rateofvaccination":[],"date":[]}
districtid_val=[]
populationleft_val=[]
rateofvaccination_val=[]
date_val=[]


# In[ ]:





# In[73]:


col_list1=df1["07/08/2021.3"].to_list()
col_list2=df1["14/08/2021.3"].to_list()


# In[74]:


ind=0
dist_data=[]
for i in state_lst:
    idx=[j for j in range(len(Dist_Name)) if Dist_Name[j].lower()==i.lower() and lvl[j]=="STATE"]
    for k in idx:
        if (tru[k]=="Total"):
            ind=k
            dist_data.append(Dist_Name[ind])
            districtid_val.append(i)
            pop=total[ind]
            inx=[]
            for l in range(len(state_code)):
                if state_code[l].lower()==Dist_Name[ind].lower() and lvl[ind]=="STATE":
                    inx.append(l)
            d0l=[]
            d1l=[]
            for leng1 in inx:
                d0l.append(col_list1[leng1])
            d0=sum(d0l)
            for leng2 in inx:
                d1l.append(col_list2[leng2])
            d1=sum(d1l)
            weekpop=d1-d0
            vac_rat=weekpop/7
            rateofvaccination_val.append(vac_rat)
            pop_lft=pop-d1
            populationleft_val.append(pop_lft)
            present_date=datetime.datetime(2021,8,14)
            while pop_lft>0:
                pop_lft=pop_lft-vac_rat
                present_date+=datetime.timedelta(days=1)
            cmplt_date=present_date.strftime("%d/%m/%Y")
            date_val.append(cmplt_date)


# In[75]:





# In[76]:


state_wise["stateid"]=districtid_val
state_wise["populationleft"]=populationleft_val
state_wise["rateofvaccination"]=rateofvaccination_val
state_wise["date"]=date_val


# In[77]:


final_frame=pd.DataFrame.from_dict(state_wise)
final_frame.sort_values(["stateid"]).to_csv(r'complete-vaccination.csv',index=False)


# In[ ]:




