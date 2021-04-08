#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Constants as c, Quartile as q
import networkx as nx


# In[2]:


class MinimumSpanningTree:
    def __init__(self, G, num_of_nodes):
        self.mst = nx.minimum_spanning_tree(G)
        self.mst_edges = []
        self.added_mst_edges = set()
        self.mst_weight = []
        self.node_u_degree = []
        self.node_v_degree = []
        self.num_of_nodes = num_of_nodes
        
    def add_mst_features(self, node_u, node_v, weight):
        self.add_mst_edge(node_u, node_v)
        self.add_mst_weight(weight)
        self.node_u_degree.append(self.get_mst_node_degree(node_u))
        self.node_v_degree.append(self.get_mst_node_degree(node_v))
        
    def add_mst_edge(self, node_u, node_v):
        is_mst_edge = 0
        
        if self.check_edge_is_legal(node_u, node_v):
            is_mst_edge = 1
        else:
            is_mst_edge = 0
            
        self.mst_edges.append(is_mst_edge / self.num_of_nodes)
        
    def add_mst_weight(self, weight):
        self.mst_weight.append(weight)
        
    def get_mst_node_degree(self, nodeID):
        for (node, degree) in self.mst.degree:
            if node == nodeID:
                return degree / self.num_of_nodes
        
    def check_edge_is_legal(self, node_u, node_v):
        return (not (self.is_added_edge(node_u, node_v) and self.is_added_edge(node_v, node_u))) and (self.is_mst_edge(node_u, node_v) or self.is_mst_edge(node_v, node_u))
        
    def is_added_edge(self, node_u, node_v):
        return (node_u, node_v) in self.added_mst_edges

    def is_mst_edge(self, node_u, node_v):
        return (node_u, node_v) in self.mst.edges
    
    def getMST(self):
        return self.mst.degree
    
    def add_to_df(self, df):
        first_q, second_q, third_q, fourth_q = q.calc_quartiles(self.node_u_degree, self.num_of_nodes)
        
        df[c.MST_U_DEGREE_1ST_QUARTILE] = first_q
        df[c.MST_U_DEGREE_2ND_QUARTILE] = second_q
        df[c.MST_U_DEGREE_3RD_QUARTILE] = third_q
        df[c.MST_U_DEGREE_4TH_QUARTILE] = fourth_q
        
        first_q, second_q, third_q, fourth_q = q.calc_quartiles(self.node_v_degree, self.num_of_nodes)
        
        df[c.MST_V_DEGREE_1ST_QUARTILE] = first_q
        df[c.MST_V_DEGREE_2ND_QUARTILE] = second_q
        df[c.MST_V_DEGREE_3RD_QUARTILE] = third_q
        df[c.MST_V_DEGREE_4TH_QUARTILE] = fourth_q
        
        first_q, second_q, third_q, fourth_q = q.calc_quartiles(self.mst_weight, self.num_of_nodes)
        
        df[c.MST_WEIGHT_1ST_QUARTILE] = first_q
        df[c.MST_WEIGHT_2ND_QUARTILE] = second_q
        df[c.MST_WEIGHT_3RD_QUARTILE] = third_q
        df[c.MST_WEIGHT_4TH_QUARTILE] = fourth_q
        
        df[c.IS_MST_EDGE] = self.mst_edges
        df[c.MST_WEIGHT] = self.mst_weight
        df[c.MST_U_DEGREE] = self.node_u_degree
        df[c.MST_V_DEGREE] = self.node_v_degree
        
        return df

