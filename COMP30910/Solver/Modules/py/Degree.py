#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Constants as c


# In[1]:


class Degree:
    def __init__(self, G):
        self.degrees = G.degree
        self.u_node_degree = []
        self.v_node_degree = []
        self.node_average_degree = []
        
    def add_degrees(self, node_u, node_v):
        node_u_degree = self.degrees[node_u]
        node_v_degree = self.degrees[node_v]

        self.u_node_degree.append(node_u_degree)
        self.v_node_degree.append(node_v_degree)
        self.node_average_degree.append((node_u_degree + node_v_degree) / 2)
    
    def add_to_df(self, df):
        df[c.U_NODE_DEGREE] = self.u_node_degree
        df[c.V_NODE_DEGREE] = self.v_node_degree
        df[c.AVERAGE_NODE_DEGREE] = self.node_average_degree
        
        return df

