#!/usr/bin/env python
# coding: utf-8

# Clustering class to calculate clustering features


import Constants as c, Quartile as q
import networkx as nx

class Clustering:
    def __init__(self, G, num_of_nodes):
        # Creates a dictionary we can query the key using a node ID
        self.clustering = nx.clustering(G, weight=c.EDGE_WEIGHT_NON_NORMALISED)
        self.u_node_clustering = []
        self.v_node_clustering = []
        self.average_node_clustering = []
        self.num_of_nodes = num_of_nodes
    
    def add_clusterings(self, node_u, node_v):
        node_u_clustering = self.clustering[node_u] / self.num_of_nodes
        node_v_clustering = self.clustering[node_v] / self.num_of_nodes
        
        self.u_node_clustering.append(node_u_clustering)
        self.v_node_clustering.append(node_v_clustering)
        self.average_node_clustering.append((node_u_clustering + node_v_clustering) / 2)
    
    def add_to_df(self, df):
        
        # Calculating quartiles
        quartile = q.Quartile(self.u_node_clustering)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()
        
        df[c.U_NODE_CLUSTERING_1ST_QUARTILE] = first_q
        df[c.U_NODE_CLUSTERING_2ND_QUARTILE] = second_q
        df[c.U_NODE_CLUSTERING_3RD_QUARTILE] = third_q
        df[c.U_NODE_CLUSTERING_4TH_QUARTILE] = fourth_q
        
         # Calculating quartiles
        quartile = q.Quartile(self.v_node_clustering)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()
        
        df[c.V_NODE_CLUSTERING_1ST_QUARTILE] = first_q
        df[c.V_NODE_CLUSTERING_2ND_QUARTILE] = second_q
        df[c.V_NODE_CLUSTERING_3RD_QUARTILE] = third_q
        df[c.V_NODE_CLUSTERING_4TH_QUARTILE] = fourth_q
        
        
        df[c.U_NODE_CLUSTERING] = self.u_node_clustering
        df[c.V_NODE_CLUSTERING] = self.v_node_clustering
        df[c.AVERAGE_NODE_CLUSTERING] = self.average_node_clustering
        
        return df

