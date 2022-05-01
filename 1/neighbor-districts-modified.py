#!/usr/bin/env python
# coding: utf-8

# In[13]:


import json
import pandas as pd
from collections import OrderedDict


# In[14]:


nd= open('neighbor_districts_cleaned.json',)
data_dict= json.load(nd)


# In[15]:


new_list=[]
for i in data_dict:
    indx=i.index('/Q')
    new_key = i[:indx]
    newkeydist=new_key.replace("_"," ")
    newkey = newkeydist.replace(" district","")
    new_list.append(newkey)
new_data_dict = dict(zip(new_list, list(data_dict.values())))


# In[16]:


new_val_dict={}
for key in new_data_dict:
    val_list=[]
    for i in new_data_dict[key]:
        indx_key=i.index('/')
        new_val_key = i[:indx_key]
        newvalkeydist = new_val_key.replace("_"," ")
        newvalkey=newvalkeydist.replace(" district","")
        val_list.append(newvalkey)
    new_val_dict[key]=val_list


# In[17]:


distcode_dict={}
cleaned_dict=new_val_dict
cowin_data=pd.read_csv("cowin_vaccine_data_districtwise_cleaned.csv")
dist_lst=cowin_data['District'].tolist()
dist_code=cowin_data['District_Key'].tolist()
distcode_dict=dict(zip(dist_lst,dist_code))


# In[18]:


new_list2=[]
for i in cleaned_dict:
    for j in distcode_dict :
        if i.lower()==j.lower():
            new_key=distcode_dict[j]
            new_list2.append(new_key)
new_data_dict2 = dict(zip(new_list2, list(cleaned_dict.values())))


# In[20]:


fnl_dict={}
for key in new_data_dict2:
    val_list=[]
    for i in new_data_dict2[key]:
        for j in distcode_dict :
            if i.lower()==j.lower():
                new_val=distcode_dict[j]
                val_list.append(new_val)
        fnl_dict[key]=val_list
fnl1_dict=OrderedDict(sorted(fnl_dict.items()))
json.dump(fnl1_dict,open("neighbor-districts-modified.json","w"))


# In[ ]:




