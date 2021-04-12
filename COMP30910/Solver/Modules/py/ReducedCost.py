import Constants as c, Quartile as q

class ReducedCost:
    def __init__(self, reduced_cost_dict, num_of_nodes):
        self.reduced_cost_dict = reduced_cost_dict
        self.reduced_cost = []
        self.num_of_nodes = num_of_nodes

    def add_reduced_cost(self, node_u, node_v):
        num = self.reduced_cost_dict[(int(node_u) - 1, int(node_v) - 1)]
        self.reduced_cost.append(num / self.num_of_nodes)

    def add_to_df(self, df):
        quartile = q.Quartile(self.reduced_cost)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()  
        
        
        df[c.REDUCED_COST_1ST_QUARTILE] = first_q
        df[c.REDUCED_COST_2ND_QUARTILE] = second_q
        df[c.REDUCED_COST_3RD_QUARTILE] = third_q
        df[c.REDUCED_COST_4TH_QUARTILE] = fourth_q
        
        df[c.REDUCED_COST] = self.reduced_cost