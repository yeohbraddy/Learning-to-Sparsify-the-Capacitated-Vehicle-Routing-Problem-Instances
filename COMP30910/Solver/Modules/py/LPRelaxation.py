import Constants as c, Quartile as q

class LPRelaxation:
    def __init__(self, lp_relaxation_dict, num_of_nodes):
        self.lp_relaxation_dict = lp_relaxation_dict
        self.relaxation = []
        self.num_of_nodes = num_of_nodes

    def add_relaxation(self, node_u, node_v):
        num = self.lp_relaxation_dict[(int(node_u) - 1, int(node_v) - 1)]
        self.relaxation.append(num / self.num_of_nodes)
    
    def add_to_df(self, df):        
        df[c.LP_RELAXATION] = self.relaxation
