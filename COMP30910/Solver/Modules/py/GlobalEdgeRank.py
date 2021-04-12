#!/usr/bin/env python
# coding: utf-8

# In[1]:


import Constants as c, Quartile as q


# In[2]:


class GlobalEdgeRank:
    def __init__(self, global_ranking_dict, num_of_nodes):
        self.global_ranking_dict = self.sort_global_ranks(global_ranking_dict)
        self.global_edge_rank = []
        self.num_of_nodes = num_of_nodes
        
    def add_ranking(self, edge_weight):
        self.global_edge_rank.append(self.global_ranking_dict[edge_weight])

    def sort_global_ranks(self, global_ranking_dict):
        return {key: rank for rank, key in enumerate(sorted(set(global_ranking_dict.values()), reverse=True), 1)}
    
    def add_to_df(self, df):

        quartile = q.Quartile(self.global_edge_rank)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()   
                
        df[c.GLOBAL_EDGE_RANK_1ST_QUARTILE] = first_q
        df[c.GLOBAL_EDGE_RANK_2ND_QUARTILE] = second_q
        df[c.GLOBAL_EDGE_RANK_3RD_QUARTILE] = third_q
        df[c.GLOBAL_EDGE_RANK_4TH_QUARTILE] = fourth_q
        
        df[c.GLOBAL_RANK] = self.global_edge_rank
    
        return df

