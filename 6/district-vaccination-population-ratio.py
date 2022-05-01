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
df=pd.DataFrame(num,columns=["District_Key","14/08/2021.5","14/08/2021.6"])
dist_code_lst=df.District_Key.to_list()


num2= pd.read_excel("Census Data.xlsx")
df2=pd.DataFrame(num2,columns=["Name","TRU","TOT_P","TOT_M","TOT_F"])
Dist_Name=df2.Name.to_list()
tru=df2.TRU.to_list()
total=df2.TOT_P.to_list()
totalm=df2.TOT_M.to_list()
totalf=df2.TOT_F.to_list()

n=open('neighbor-districts-modified.json',)
data=json.load(n)


# In[3]:


df1=df.drop([0],axis=0)
cols = df1.columns.drop('District_Key')
df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')
dist_code=df1.District_Key.to_list()
dist_code_lst=df1.District_Key


# In[4]:





# In[5]:


district_wise={"districtid":[],"vaccinationratio":[],"populationratio":[],"ratioofratios":[]}
districtid_val=[]
vaccinationratio_val=[]
populationratio_val=[]
ratioofratios_val=[]


# In[6]:


col_listm=df1["14/08/2021.5"].to_list()
col_listf=df1["14/08/2021.6"].to_list()


# In[7]:


ind=0
dist_data=[]
for i in data:
    idx=[j for j in range(len(Dist_Name)) if Dist_Name[j]==i[3:]]
    for k in idx:
        if (tru[k]=="Total"):
            ind=k
            dist_data.append(Dist_Name[ind])
            districtid_val.append(i)
            m=totalm[ind]
            f=totalf[ind]
            pr=f/m
            populationratio_val.append(pr)
            for l in dist_code:
                if l[3:]==Dist_Name[ind]:
                    inx=dist_code.index(l)
            mv=col_listm[inx]
            fv=col_listf[inx]
            vr=fv/mv
            vaccinationratio_val.append(vr)
            pvr=vr/pr
            ratioofratios_val.append(pvr)
                    


# In[8]:





# In[9]:


district_wise["districtid"]=districtid_val
district_wise["vaccinationratio"]=vaccinationratio_val
district_wise["populationratio"]=populationratio_val
district_wise["ratioofratios"]=ratioofratios_val


# In[10]:


final_frame=pd.DataFrame.from_dict(district_wise)
final_frame.sort_values(["districtid"]).to_csv(r'district-vaccination-population-ratio.csv',index=False)


# In[ ]:




