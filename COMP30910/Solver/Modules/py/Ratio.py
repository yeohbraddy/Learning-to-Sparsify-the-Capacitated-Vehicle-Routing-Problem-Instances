import Constants as c

class Ratio:
    def __init__(self, demands, capacity, num_of_nodes):
        self.demands = demands
        self.capacity = capacity
        self.demand_capacity_ratio_node_u = []
        self.demand_capacity_ratio_node_v = []
        self.num_of_nodes = num_of_nodes

    def add_ratios(self, node_u, node_v):
        ratio = self.calculate_demand_to_capacity(node_u)
        self.demand_capacity_ratio_node_u.append(ratio)

        ratio = self.calculate_demand_to_capacity(node_v)
        self.demand_capacity_ratio_node_v.append(ratio)

    def calculate_demand_to_capacity(self, node_id):
        return self.demands[int(node_id)] / self.capacity

    def add_to_df(self, df):
        df[c.U_NODE_DEMAND_CAPACITY_RATIO] = self.demand_capacity_ratio_node_u
        df[c.V_NODE_DEMAND_CAPACITY_RATIO] = self.demand_capacity_ratio_node_v