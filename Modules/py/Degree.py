#!/usr/bin/env python
# coding: utf-8

# Degree class to calculate degree features


import Constants as c, Quartile as q
import numpy as np
import networkx as nx

class Degree:
    def __init__(self, G, num_of_nodes):
        # Creates a dictionary we can query the key using a node ID
        self.degrees = G.degree(weight=c.EDGE_WEIGHT_NON_NORMALISED)
        self.temp = G.degree()
        self.u_node_degree = []
        self.v_node_degree = []
        self.node_average_degree = []
        self.num_of_nodes = num_of_nodes
        # Creates a dictionary we can query the key using a node ID
        self.generalized_degree = nx.generalized_degree(G)
        self.node_u_edge_triangle_multiplicity = []
        self.node_v_edge_triangle_multiplicity = []
        self.node_average_edge_triangle_multiplicity = []
        self.node_u_edge_generalised_degree = []
        self.node_v_edge_generalised_degree = []
        self.node_average_generalised_degree = []
        # Creates a dictionary we can query the key using a node ID
        self.knn = nx.k_nearest_neighbors(G, weight=c.EDGE_WEIGHT_NON_NORMALISED)
        self.node_u_k_nearest_neighbors = []
        self.node_v_k_nearest_neighbors = []
        self.node_average_k_nearest_neighbors = []
        
        
    def add_degrees(self, node_u, node_v):
        node_u_degree = self.degrees[node_u] / self.num_of_nodes
        node_v_degree = self.degrees[node_v] / self.num_of_nodes

        self.u_node_degree.append(node_u_degree)
        self.v_node_degree.append(node_v_degree)
        self.node_average_degree.append((node_u_degree + node_v_degree) / 2)
        
        # Query by the node which returns a Counter where the key indicates the edge triangle multiplicity and the value is 
        # the generalised degree
        key = list(self.generalized_degree[node_u].keys())[0]
        node_u_edge_triangle_multiplicity = key / self.num_of_nodes
        node_u_edge_generalised_degree = self.generalized_degree[node_u][key] / self.num_of_nodes
        
        
        key = list(self.generalized_degree[node_v].keys())[0]
        node_v_edge_triangle_multiplicity = key / self.num_of_nodes
        node_v_edge_generalised_degree = self.generalized_degree[node_v][key] / self.num_of_nodes
        
        self.node_u_edge_triangle_multiplicity.append(node_u_edge_triangle_multiplicity)
        self.node_v_edge_triangle_multiplicity.append(node_v_edge_triangle_multiplicity)
        self.node_average_edge_triangle_multiplicity.append((node_u_edge_triangle_multiplicity + node_v_edge_triangle_multiplicity) / 2)
        
        self.node_u_edge_generalised_degree.append(node_u_edge_generalised_degree)
        self.node_v_edge_generalised_degree.append(node_v_edge_generalised_degree)
        self.node_average_generalised_degree.append((node_u_edge_generalised_degree + node_v_edge_generalised_degree) / 2)
        
        node_u_knn = self.knn[self.temp[node_u]] / self.num_of_nodes
        node_v_knn = self.knn[self.temp[node_v]] / self.num_of_nodes
        
        self.node_u_k_nearest_neighbors.append(node_u_knn)
        self.node_v_k_nearest_neighbors.append(node_v_knn)
        self.node_average_k_nearest_neighbors.append((node_u_knn + node_v_knn) / 2)
    
    def add_to_df(self, df):
        # Calculating quartiles
        quartile = q.Quartile(self.u_node_degree)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()       
        
        df[c.U_NODE_DEGREE_1ST_QUARTILE] = first_q
        df[c.U_NODE_DEGREE_2ND_QUARTILE] = second_q
        df[c.U_NODE_DEGREE_3RD_QUARTILE] = third_q
        df[c.U_NODE_DEGREE_4TH_QUARTILE] = fourth_q
  
        # Calculating quartiles
        quartile = q.Quartile(self.v_node_degree)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()     
                
        df[c.V_NODE_DEGREE_1ST_QUARTILE] = first_q
        df[c.V_NODE_DEGREE_2ND_QUARTILE] = second_q
        df[c.V_NODE_DEGREE_3RD_QUARTILE] = third_q
        df[c.V_NODE_DEGREE_4TH_QUARTILE] = fourth_q   
        
        # Calculating quartiles
        quartile = q.Quartile(self.node_u_edge_triangle_multiplicity)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()     
                
        df[c.NODE_U_EDGE_TRIANGLE_MULTIPLICITY_1ST_QUARTILE] = first_q
        df[c.NODE_U_EDGE_TRIANGLE_MULTIPLICITY_2ND_QUARTILE] = second_q
        df[c.NODE_U_EDGE_TRIANGLE_MULTIPLICITY_3RD_QUARTILE] = third_q
        df[c.NODE_U_EDGE_TRIANGLE_MULTIPLICITY_4TH_QUARTILE] = fourth_q   
        
        # Calculating quartiles
        quartile = q.Quartile(self.node_v_edge_triangle_multiplicity)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()     
                
        df[c.NODE_V_EDGE_TRIANGLE_MULTIPLICITY_1ST_QUARTILE] = first_q
        df[c.NODE_V_EDGE_TRIANGLE_MULTIPLICITY_2ND_QUARTILE] = second_q
        df[c.NODE_V_EDGE_TRIANGLE_MULTIPLICITY_3RD_QUARTILE] = third_q
        df[c.NODE_V_EDGE_TRIANGLE_MULTIPLICITY_4TH_QUARTILE] = fourth_q
        
        # Calculating quartiles
        quartile = q.Quartile(self.node_u_edge_generalised_degree)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()     
                
        df[c.NODE_U_EDGE_GENERALISED_DEGREE_1ST_QUARTILE] = first_q
        df[c.NODE_U_EDGE_GENERALISED_DEGREE_2ND_QUARTILE] = second_q
        df[c.NODE_U_EDGE_GENERALISED_DEGREE_3RD_QUARTILE] = third_q
        df[c.NODE_U_EDGE_GENERALISED_DEGREE_4TH_QUARTILE] = fourth_q   
        
        # Calculating quartiles
        quartile = q.Quartile(self.node_v_edge_generalised_degree)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()     
                
        df[c.NODE_V_EDGE_GENERALISED_DEGREE_1ST_QUARTILE] = first_q
        df[c.NODE_V_EDGE_GENERALISED_DEGREE_2ND_QUARTILE] = second_q
        df[c.NODE_V_EDGE_GENERALISED_DEGREE_3RD_QUARTILE] = third_q
        df[c.NODE_V_EDGE_GENERALISED_DEGREE_4TH_QUARTILE] = fourth_q   
        
                
        df[c.U_NODE_DEGREE] = self.u_node_degree
        df[c.V_NODE_DEGREE] = self.v_node_degree
        df[c.AVERAGE_NODE_DEGREE] = self.node_average_degree
        
        df[c.NODE_U_EDGE_TRIANGLE_MULTIPLICITY] = self.node_u_edge_triangle_multiplicity
        df[c.NODE_V_EDGE_TRIANGLE_MULTIPLICITY] = self.node_v_edge_triangle_multiplicity
        df[c.NODE_AVERAGE_EDGE_TRIANGLE_MULTIPLICITY] = self.node_average_edge_triangle_multiplicity
        
        df[c.NODE_U_EDGE_GENERALISED_DEGREE] = self.node_u_edge_generalised_degree
        df[c.NODE_V_EDGE_GENERALISED_DEGREE] = self.node_v_edge_generalised_degree
        df[c.NODE_AVERAGE_EDGE_GENERALISED_DEGREE] = self.node_average_generalised_degree
        
        df[c.NODE_U_AVERAGE_DEGREE_CONNECTIVITY] = self.node_u_k_nearest_neighbors
        df[c.NODE_V_AVERAGE_DEGREE_CONNECTIVITY] = self.node_v_k_nearest_neighbors
        df[c.NODE_AVERAGE_AVERAGE_DEGREE_CONNECTIVITY] = self.node_average_k_nearest_neighbors
        
        return df

