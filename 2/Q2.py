#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd
import csv


# In[2]:


n=open('neighbor-districts-modified.json',)
neighbor_dict=json.load(n)
csv_file=open('edge-graph.csv','w', newline='')
file_obj=csv.writer(csv_file)


# In[3]:


new_neighbor_dict={}
count=0
for i in neighbor_dict:
    for j in neighbor_dict[i]:
        tupl=(i,j)
        print(tupl)
        count=count+1
        file_obj.writerow(tupl)
print(count)


# In[ ]:





# In[ ]:




