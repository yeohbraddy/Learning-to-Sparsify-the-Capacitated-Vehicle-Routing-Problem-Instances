#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Constants as c


# In[2]:


class LocalEdgeRank:
    def __init__(self, incidenceMatrix):
        self.incidenceMatrix = incidenceMatrix
        self.u_node_local_edge_rank = []
        self.v_node_local_edge_rank = []
        
    def addRankings(self, node_u, node_v):
        self.u_node_local_edge_rank.append(self.calculateLocalRank(node_u, node_v))
        self.v_node_local_edge_rank.append(self.calculateLocalRank(node_v, node_u))     
        
    def calculateLocalRank(self, node_u, node_v):
        row = self.incidenceMatrix[node_u]
        sorted_row = row.sort_values(ascending=True)
        
        return sorted_row[node_v]
    
    def addToDF(self, df):
        df[c.U_NODE_LOCAL_EDGE_RANK] = self.u_node_local_edge_rank
        df[c.V_NODE_LOCAL_EDGE_RANK] = self.v_node_local_edge_rank
        
        return df

