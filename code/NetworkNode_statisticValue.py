#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas import Series , DataFrame


# In[2]:


nodes_list = pd.read_csv('../data/node2016.csv')


# In[3]:


nodes_list1 = list(nodes_list['id'])


# In[4]:


edges_list = pd.read_csv('../data/2016_gephi.csv')


# In[5]:


edges_list1 = edges_list.values.tolist()


# In[6]:


import networkx as nx
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# In[7]:


G = nx.Graph()
G.add_nodes_from(nodes_list1)
G.add_edges_from(edges_list1)


# In[8]:


degree = nx.degree_centrality(G)
closeness = nx.closeness_centrality(G)
betweenness = nx.betweenness_centrality(G)


# In[9]:


df = {
    "Degree centrality" : degree,
    "Betweenness centrality" : betweenness,
    "Closeness centrality" : closeness
    
    
}


# In[10]:


df_sta = DataFrame(df)
df_sta


# In[11]:


df_sta.sort_values(by = ['Degree centrality'],axis = 0,ascending = False).head(6)


# In[12]:


df_sta.sort_values(by = ['Betweenness centrality'],axis = 0,ascending = False).head(6)


# In[13]:


df_sta.sort_values(by = ['Closeness centrality'],axis = 0,ascending = False).head(6)


# In[14]:


#Computing network density
nx.density(G)

