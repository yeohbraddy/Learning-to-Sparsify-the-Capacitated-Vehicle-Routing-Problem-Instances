#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Constants as c


# In[2]:


class GlobalEdgeRank:
    def __init__(self, global_ranking_dict):
        self.global_ranking_dict = self.sortGlobalRanks(global_ranking_dict)
        self.global_edge_rank = []
        
    def addRanking(self, edge_weight):
        self.global_edge_rank.append(self.global_ranking_dict[edge_weight])

    def sortGlobalRanks(self, global_ranking_dict):
        return {key: rank for rank, key in enumerate(sorted(set(global_ranking_dict.values()), reverse=True), 1)}

    def addToDF(self, df):
        df[c.GLOBAL_RANK] = self.global_edge_rank
    
        return df

