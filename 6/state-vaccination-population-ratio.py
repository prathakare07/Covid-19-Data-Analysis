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
df=pd.DataFrame(num,columns=["State","14/08/2021.5","14/08/2021.6"])
dist_code_lst=df.State.to_list()


num2= pd.read_excel("Census Data.xlsx")
df2=pd.DataFrame(num2,columns=["Level","Name","TRU","TOT_P","TOT_M","TOT_F"])
Dist_Name=df2.Name.to_list()
tru=df2.TRU.to_list()
total=df2.TOT_P.to_list()
totalm=df2.TOT_M.to_list()
totalf=df2.TOT_F.to_list()
lvl=df2.Level.to_list()


# In[5]:


df1=df.drop([0],axis=0)
cols = df1.columns.drop('State')
df1[cols] = df1[cols].apply(pd.to_numeric, errors='coerce')
state_code=df1.State.to_list()


# In[6]:





# In[13]:


state_wise={"stateid":[],"vaccinationratio":[],"populationratio":[],"ratioofratios":[]}
districtid_val=[]
vaccinationratio_val=[]
populationratio_val=[]
ratioofratios_val=[]


# In[14]:


state_lst=['Himachal Pradesh','Haryana','Andhra Pradesh','Arunachal Pradesh','Assam','Bihar','Chhattisgarh','Goa','Gujarat','Jharkhand','Karnataka','Kerala',
            'Madhya Pradesh','Maharashtra','Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Punjab','Rajasthan','Sikkim','Tamil Nadu',
            'Telangana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal','Andaman and Nicobar Islands','Dadra and Nagar Haveli and Daman and Diu',
            'Jammu and Kashmir','Lakshadweep','Chandigarh','Delhi','Ladakh','Puducherry']
state_values=[]
k=0
for i in range(len(state_lst)):
    state_values.append(k)
state_dict=dict(zip(state_lst,state_values))


# In[15]:


col_listm=df1["14/08/2021.5"].to_list()
col_listf=df1["14/08/2021.6"].to_list()


# In[16]:


ind=0
dist_data=[]
for i in state_lst:
    idx=[j for j in range(len(Dist_Name)) if Dist_Name[j].lower()==i.lower() and lvl[j]=="STATE"]
    for k in idx:
        if (tru[k]=="Total"):
            ind=k
            dist_data.append(Dist_Name[ind])
            districtid_val.append(i)
            m=totalm[ind]
            f=totalf[ind]
            pr=f/m
            populationratio_val.append(pr)
            inx=[]
            for l in range(len(state_code)):
                if state_code[l].lower()==Dist_Name[k].lower() and lvl[k]=="STATE":
                    inx.append(l)
            mvl=[]
            fvl=[]
            for leng1 in inx:
                mvl.append(col_listm[leng1])
            mv=sum(mvl)
            for leng2 in inx:
                fvl.append(col_listf[leng2])
            fv=sum(fvl)
            vr=fv/mv
            vaccinationratio_val.append(vr)
            pvr=vr/pr
            ratioofratios_val.append(pvr)
                    


# In[17]:





# In[18]:


state_wise["stateid"]=districtid_val
state_wise["vaccinationratio"]=vaccinationratio_val
state_wise["populationratio"]=populationratio_val
state_wise["ratioofratios"]=ratioofratios_val


# In[19]:


final_frame=pd.DataFrame.from_dict(state_wise)
final_frame.sort_values(["statename"]).to_csv(r'state-vaccination-population-ratio.csv',index=False)


# In[ ]:




