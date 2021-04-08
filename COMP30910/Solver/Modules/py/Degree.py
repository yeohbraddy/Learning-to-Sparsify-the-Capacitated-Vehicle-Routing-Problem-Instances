#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import Constants as c, Quartile as q
import numpy as np


# In[1]:


class Degree:
    def __init__(self, G, num_of_nodes):
        self.degrees = G.degree
        self.u_node_degree = []
        self.v_node_degree = []
        self.node_average_degree = []
        self.num_of_nodes = num_of_nodes
        
    def add_degrees(self, node_u, node_v):
        node_u_degree = self.degrees[node_u] / self.num_of_nodes
        node_v_degree = self.degrees[node_v] / self.num_of_nodes

        self.u_node_degree.append(node_u_degree)
        self.v_node_degree.append(node_v_degree)
        self.node_average_degree.append((node_u_degree + node_v_degree) / 2)

    
    def add_to_df(self, df):
        
        first_q, second_q, third_q, fourth_q = q.calc_quartiles(self.u_node_degree, self.num_of_nodes)
        
        df[c.U_NODE_DEGREE_1ST_QUARTILE] = first_q
        df[c.U_NODE_DEGREE_2ND_QUARTILE] = second_q
        df[c.U_NODE_DEGREE_3RD_QUARTILE] = third_q
        df[c.U_NODE_DEGREE_4TH_QUARTILE] = fourth_q
        
        first_q, second_q, third_q, fourth_q = q.calc_quartiles(self.v_node_degree, self.num_of_nodes)
        
        df[c.V_NODE_DEGREE_1ST_QUARTILE] = first_q
        df[c.V_NODE_DEGREE_2ND_QUARTILE] = second_q
        df[c.V_NODE_DEGREE_3RD_QUARTILE] = third_q
        df[c.V_NODE_DEGREE_4TH_QUARTILE] = fourth_q                
                
        df[c.U_NODE_DEGREE] = self.u_node_degree
        df[c.V_NODE_DEGREE] = self.v_node_degree
        df[c.AVERAGE_NODE_DEGREE] = self.node_average_degree
        
        return df

