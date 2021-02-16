#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Constants as c
import networkx as nx


# In[2]:


class MinimumSpanningTree:
    def __init__(self, G):
        self.MST = nx.minimum_spanning_tree(G)
        self.mstEdges = []
        self.addedMstEdges = set()
        self.mstWeight = []
        self.node_u_degree = []
        self.node_v_degree = []
        
    def addMSTFeatures(self, node_u, node_v, weight):
        self.addMSTEdge(node_u, node_v)
        self.addMSTWeight(weight)
        self.node_u_degree.append(self.getMSTNodeDegree(node_u))
        self.node_v_degree.append(self.getMSTNodeDegree(node_v))
        
    def addMSTEdge(self, node_u, node_v):
        isMSTEdge = 0
        
        if self.checkEdgeIsLegal(node_u, node_v):
            isMSTEdge = 1
        else:
            isMSTEdge = 0
            
        self.mstEdges.append(isMSTEdge)
        
    def addMSTWeight(self, weight):
        self.mstWeight.append(weight)
        
    def getMSTNodeDegree(self, nodeID):
        for (node, degree) in self.MST.degree:
            if node == nodeID:
                return degree
        
    def checkEdgeIsLegal(self, node_u, node_v):
        return (not (self.isAddedEdge(node_u, node_v) and                      self.isAddedEdge(node_v, node_u))) and (self.isMSTEdge(node_u, node_v) or                      self.isMSTEdge(node_v, node_u))
        
    def isAddedEdge(self, node_u, node_v):
        return (node_u, node_v) in self.addedMstEdges

    def isMSTEdge(self, node_u, node_v):
        return (node_u, node_v) in self.MST.edges
    
    def getMST(self):
        return self.MST.degree
    
    def addToDF(self, df):
        df[c.IS_MST_EDGE] = self.mstEdges
        df[c.MST_WEIGHT] = self.mstWeight
        df[c.MST_U_DEGREE] = self.node_u_degree
        df[c.MST_V_DEGREE] = self.node_v_degree
        
        return df

