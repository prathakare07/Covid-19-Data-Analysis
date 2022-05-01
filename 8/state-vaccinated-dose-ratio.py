#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import csv
import pandas as pd
import numpy as np
from pandas import ExcelFile


# In[2]:


num=pd.read_csv("cowin_vaccine_data_districtwise.csv")
df=pd.DataFrame(num,columns=["State","14/08/2021.3","14/08/2021.4"])
dist_code_lst=df.State.to_list()


num2= pd.read_excel("Census Data.xlsx")
df2=pd.DataFrame(num2,columns=["Level","Name","TRU","TOT_P"])
Dist_Name=df2.Name.to_list()
tru=df2.TRU.to_list()
total=df2.TOT_P.to_list()
lvl=df2.Level.to_list()

n=open('neighbor-districts-modified.json',)
data=json.load(n)


# In[3]:


df1=df.drop([0],axis=0)
cols = df1.columns.drop('State')
df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')
state_code=df1.State.to_list()


# In[8]:


state_wise={"statename":[],"vaccinateddose1ratio":[],"vaccinateddose2ratio":[],}
statename_val=[]
vaccinateddose1_val=[]
vaccinateddose2_val=[]


# In[9]:


col_list1=df1["14/08/2021.3"].to_list()
col_list2=df1["14/08/2021.4"].to_list()


# In[10]:


state_lst=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']
state_values=[]
k=0
for i in range(len(state_lst)):
    state_values.append(k)
state_dict=dict(zip(state_lst,state_values))


# In[11]:


ind=0
dist_data=[]
for i in state_lst:
    idx=[j for j in range(len(Dist_Name)) if Dist_Name[j].lower()==i.lower() and lvl[j]=="STATE"]
    for k in idx:
        if (tru[k]=="Total"):
            ind=k
            dist_data.append(Dist_Name[ind])
            statename_val.append(i)
            ttl=total[ind]
            inx=[]
            for l in range(len(state_code)):
                if state_code[l].lower()==Dist_Name[ind].lower() and lvl[ind]=="STATE":
                    inx.append(l)
            d1l=[]
            d2l=[]
            for leng1 in inx:
                d1l.append(col_list1[leng1])
            d1=sum(d1l)
            for leng2 in inx:
                d2l.append(col_list2[leng2])
            d2=sum(d2l)
            d1_r=d1/ttl
            vaccinateddose1_val.append(d1_r)
            d2_r=d2/ttl
            vaccinateddose2_val.append(d2_r)
                    


# In[12]:





# In[13]:


state_wise["statename"]=statename_val
state_wise["vaccinateddose1ratio"]=vaccinateddose1_val
state_wise["vaccinateddose2ratio"]=vaccinateddose2_val


# In[14]:


final_frame=pd.DataFrame.from_dict(state_wise)
final_frame.sort_values(["vaccinateddose1ratio"]).to_csv(r'state-vaccinated-dose-ratio.csv',index=False)


# In[ ]:




