#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Constants as c
import networkx as nx


# In[2]:


class Clustering:
    def __init__(self, G):
        self.clustering = nx.clustering(G)
        self.u_node_clustering = []
        self.v_node_clustering = []
        self.average_node_clustering = []
    
    def add_clusterings(self, node_u, node_v):
        node_u_clustering = self.clustering[node_u]
        node_v_clustering = self.clustering[node_v]
        
        self.u_node_clustering.append(node_u_clustering)
        self.v_node_clustering.append(node_v_clustering)
        self.average_node_clustering.append((node_u_clustering + node_v_clustering) / 2)
    
    def add_to_df(self, df):
        df[c.U_NODE_CLUSTERING] = self.u_node_clustering
        df[c.V_NODE_CLUSTERING] = self.v_node_clustering
        df[c.AVERAGE_NODE_CLUSTERING] = self.average_node_clustering
        
        return df

