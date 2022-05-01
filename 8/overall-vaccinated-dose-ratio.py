#!/usr/bin/env python
# coding: utf-8

# In[5]:


import json
import csv
import pandas as pd
import numpy as np
from pandas import ExcelFile


# In[11]:


num=pd.read_csv("cowin_vaccine_data_districtwise.csv")
df=pd.DataFrame(num,columns=["State","14/08/2021.3","14/08/2021.4"])
dist_code_lst=df.State.to_list()


num2= pd.read_excel("Census Data.xlsx")
df2=pd.DataFrame(num2,columns=["Level","Name","TRU","TOT_P"])
Dist_Name=df2.Name.to_list()
tru=df2.TRU.to_list()
total=df2.TOT_P.to_list()
lvl=df2.Level.to_list()


# In[12]:


df1=df.drop([0],axis=0)
cols = df1.columns.drop('State')
df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')
state_code=df1.State.to_list()


# In[30]:


state_wise={"region":[],"vaccinateddose1ratio":[],"vaccinateddose2ratio":[],}
statename_val=[]
vaccinateddose1_val=[]
vaccinateddose2_val=[]


# In[31]:


col_list1=df1["14/08/2021.3"].to_list()
col_list2=df1["14/08/2021.4"].to_list()


# In[32]:


state_lst=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']
state_values=[]
k=0
for i in range(len(state_lst)):
    state_values.append(k)
state_dict=dict(zip(state_lst,state_values))


# In[33]:


ind=0
dist_data=[]
totalp=[]
totald1=[]
totald2=[]
for i in state_lst:
    idx=[j for j in range(len(Dist_Name)) if Dist_Name[j].lower()==i.lower() and lvl[j]=="STATE"]
    for k in idx:
        if (tru[k]=="Total"):
            ind=k
            dist_data.append(Dist_Name[ind])
            totalp.append(total[ind])
            inx=[]
            for l in state_code:
                if l.lower()==Dist_Name[k].lower() and lvl[k]=="STATE":
                    inx.append(state_code.index(l))
            vl1=[]
            vl2=[]
            for leng1 in inx:
                vl1.append(col_list1[leng1])
            totald1.append(sum(vl1))
            for leng2 in inx:
                vl2.append(col_list2[leng2])
            totald2.append(sum(vl2))
            
statename_val.append("Overall") 
sump=sum(totalp)
sumd1=sum(totald1)
sumd2=sum(totald2)
d1_r=sumd1/sump
vaccinateddose1_val.append(d1_r)
d2_r=sumd2/sump
vaccinateddose2_val.append(d2_r)


# In[34]:





# In[35]:


state_wise["region"]=statename_val
state_wise["vaccinateddose1ratio"]=vaccinateddose1_val
state_wise["vaccinateddose2ratio"]=vaccinateddose2_val


# In[36]:


final_frame=pd.DataFrame.from_dict(state_wise)
final_frame.sort_values(["vaccinateddose1ratio"]).to_csv(r'overall-vaccinated-dose-ratio.csv',index=False)


# In[ ]:




