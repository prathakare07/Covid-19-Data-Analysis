#!/usr/bin/env python
# coding: utf-8

# In[3]:


import json
import csv
import pandas as pd
import numpy as np
from pandas import ExcelFile


# In[4]:


num=pd.read_csv("cowin_vaccine_data_districtwise.csv")
df=pd.DataFrame(num,columns=["District_Key","14/08/2021.3","14/08/2021.4"])
dist_code_lst=df.District_Key.to_list()


num2= pd.read_excel("Census Data.xlsx")
df2=pd.DataFrame(num2,columns=["Name","TRU","TOT_P"])
Dist_Name=df2.Name.to_list()
tru=df2.TRU.to_list()
total=df2.TOT_P.to_list()

n=open('neighbor-districts-modified.json',)
data=json.load(n)


# In[5]:


df1=df.drop([0],axis=0)
cols = df1.columns.drop('District_Key')
df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')
dist_code=df1.District_Key.to_list()
dist_code_lst=df1.District_Key


# In[16]:


district_wise={"districtid":[],"vaccinateddose1ratio":[],"vaccinateddose2ratio":[],}
districtid_val=[]
vaccinateddose1_val=[]
vaccinateddose2_val=[]


# In[17]:


col_list1=df1["14/08/2021.3"].to_list()
col_list2=df1["14/08/2021.4"].to_list()


# In[18]:


ind=0
dist_data=[]
for i in data:
    idx=[j for j in range(len(Dist_Name)) if Dist_Name[j]==i[3:]]
    for k in idx:
        if (tru[k]=="Total"):
            ind=k
            dist_data.append(Dist_Name[ind])
            districtid_val.append(i)
            ttl=total[ind]
            for l in dist_code:
                if l[3:]==Dist_Name[ind]:
                    inx=dist_code.index(l)
            d1=col_list1[inx]
            d2=col_list2[inx]
            d1_r=d1/ttl
            vaccinateddose1_val.append(d1_r)
            d2_r=d2/ttl
            vaccinateddose2_val.append(d2_r)


# In[19]:





# In[20]:


district_wise["districtid"]=districtid_val
district_wise["vaccinateddose1ratio"]=vaccinateddose1_val
district_wise["vaccinateddose2ratio"]=vaccinateddose2_val


# In[21]:


final_frame=pd.DataFrame.from_dict(district_wise)
final_frame.sort_values(["vaccinateddose1ratio"]).to_csv(r'district-vaccinated-dose-ratio.csv',index=False)


# In[ ]:




