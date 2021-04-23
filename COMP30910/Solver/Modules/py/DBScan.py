#!/usr/bin/env python
# coding: utf-8

# DBScan class to calculate DBScan features

from sklearn.cluster import DBSCAN
import Constants as c, Quartile as q

class DBScan:
    def __init__(self, dbscan, num_of_nodes):
        # List of node coordinates, e.g, l1 = [(1, 2), ..., (2, 3)] where l1[0] = x = 1, y = 2
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
        df[c.U_NODE_DBSCAN] = self.u_node_dbscan
        df[c.V_NODE_DBSCAN] = self.v_node_dbscan
        df[c.AVERAGE_NODE_DBSCAN] = self.average_node_dbscan
        
        return df





