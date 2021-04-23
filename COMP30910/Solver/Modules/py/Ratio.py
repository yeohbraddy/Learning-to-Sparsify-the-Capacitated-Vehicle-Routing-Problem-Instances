import Constants as c, Quartile as q

# Ratio class to calculate ratio features

class Ratio:
    def __init__(self, demands, capacity, num_of_nodes):
        # Creates a dictionary we can query the key using a node ID
        self.demands = demands
        self.capacity = capacity
        self.demand_capacity_ratio_node_u = []
        self.demand_capacity_ratio_node_v = []
        self.demand_capacity_ratio_node_average = []
        self.num_of_nodes = num_of_nodes

    def add_ratios(self, node_u, node_v):
        ratio_u = self.calculate_demand_to_capacity(node_u)
        self.demand_capacity_ratio_node_u.append(ratio_u)

        ratio_v = self.calculate_demand_to_capacity(node_u)
        self.demand_capacity_ratio_node_v.append(ratio_v)
        
        self.demand_capacity_ratio_node_average.append((ratio_u + ratio_v) / 2)

    def calculate_demand_to_capacity(self, node_id):
        return self.demands[int(node_id)] / self.capacity / self.num_of_nodes

    def add_to_df(self, df): 
        df[c.U_NODE_DEMAND_CAPACITY_RATIO] = self.demand_capacity_ratio_node_u
        df[c.V_NODE_DEMAND_CAPACITY_RATIO] = self.demand_capacity_ratio_node_v
        df[c.AVERAGE_NODE_DEMAND_CAPACITY_RATIO] = self.demand_capacity_ratio_node_average
        