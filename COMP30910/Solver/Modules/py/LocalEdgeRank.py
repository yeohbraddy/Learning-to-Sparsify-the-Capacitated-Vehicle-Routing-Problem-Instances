#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Constants as c


# In[2]:


class LocalEdgeRank:
    def __init__(self, incidence_matrix, num_of_nodes):
        self.incidence_matrix = incidence_matrix
        self.u_node_local_edge_rank = []
        self.v_node_local_edge_rank = []
        self.num_of_nodes = num_of_nodes
        
    def add_rankings(self, node_u, node_v):
        self.u_node_local_edge_rank.append(self.calculate_local_rank(node_u, node_v))
        self.v_node_local_edge_rank.append(self.calculate_local_rank(node_v, node_u))     
        
    def calculate_local_rank(self, node_u, node_v):
        row = self.incidence_matrix[node_u]
        sorted_row = row.sort_values(ascending=True)
        
        return sorted_row[node_v] / self.num_of_nodes
    
    def add_to_df(self, df):
        df[c.U_NODE_LOCAL_EDGE_RANK] = self.u_node_local_edge_rank
        df[c.V_NODE_LOCAL_EDGE_RANK] = self.v_node_local_edge_rank
        
        return df

