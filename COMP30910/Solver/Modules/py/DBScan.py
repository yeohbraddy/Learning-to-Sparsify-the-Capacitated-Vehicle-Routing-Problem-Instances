#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.cluster import DBSCAN
import Constants as c, Quartile as q


# In[2]:


class DBScan:
    def __init__(self, dbscan, num_of_nodes):
        self.dbscan = dbscan
        self.u_node_dbscan = []
        self.v_node_dbscan = []
        self.average_node_dbscan = []
        self.num_of_nodes = num_of_nodes
        self.dbscan_dict = {}
        
        clustering = DBSCAN(eps=3, min_samples=2).fit(self.dbscan)
        for idx in range(0, len(self.dbscan)):
            coord = self.dbscan[idx]
            self.dbscan_dict[(coord[0], coord[1])] = clustering.labels_[idx]
    
    def add_dbscan(self, node_u, node_v):
        u_node_dbscan = self.dbscan_dict[node_u] / self.num_of_nodes
        v_node_dbscan = self.dbscan_dict[node_v] / self.num_of_nodes
        
        self.u_node_dbscan.append(u_node_dbscan)
        self.v_node_dbscan.append(v_node_dbscan)
        self.average_node_dbscan.append((u_node_dbscan + v_node_dbscan) / 2)
    
    def add_to_df(self, df):

        quartile = q.Quartile(self.u_node_dbscan)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()
        
        df[c.U_NODE_DBSCAN_1ST_QUARTILE] = first_q
        df[c.U_NODE_DBSCAN_2ND_QUARTILE] = second_q
        df[c.U_NODE_DBSCAN_3RD_QUARTILE] = third_q
        df[c.U_NODE_DBSCAN_4TH_QUARTILE] = fourth_q
        
        
        quartile = q.Quartile(self.v_node_dbscan)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()
        
        df[c.V_NODE_DBSCAN_1ST_QUARTILE] = first_q
        df[c.V_NODE_DBSCAN_2ND_QUARTILE] = second_q
        df[c.V_NODE_DBSCAN_3RD_QUARTILE] = third_q
        df[c.V_NODE_DBSCAN_4TH_QUARTILE] = fourth_q
        
        df[c.U_NODE_DBSCAN] = self.u_node_dbscan
        df[c.V_NODE_DBSCAN] = self.v_node_dbscan
        df[c.AVERAGE_NODE_DBSCAN] = self.average_node_dbscan
        
        return df


# In[ ]:




