import Constants as c, Quartile as q

# ReducedCost class to calculate reduced cost features

class ReducedCost:
    def __init__(self, reduced_cost_dict, num_of_nodes):
        # Creates a dictionary we can query the key using an edge consisting of its node IDs
        self.reduced_cost_dict = reduced_cost_dict
        self.reduced_cost = []
        self.num_of_nodes = num_of_nodes

    def add_reduced_cost(self, node_u, node_v):
        num = self.reduced_cost_dict[(int(node_u) - 1, int(node_v) - 1)]
        self.reduced_cost.append(num / self.num_of_nodes)

    def add_to_df(self, df):     
        df[c.REDUCED_COST] = self.reduced_cost