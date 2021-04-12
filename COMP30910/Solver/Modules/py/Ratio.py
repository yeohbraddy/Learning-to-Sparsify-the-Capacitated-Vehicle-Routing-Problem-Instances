import Constants as c, Quartile as q

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
        return self.demands[int(node_id)] / self.capacity / self.num_of_nodes

    def add_to_df(self, df):
        quartile = q.Quartile(self.demand_capacity_ratio_node_u)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()  
        
       
        df[c.DEMAND_CAPACITY_RATIO_NODE_U_1ST_QUARTILE] = first_q
        df[c.DEMAND_CAPACITY_RATIO_NODE_U_2ND_QUARTILE] = second_q
        df[c.DEMAND_CAPACITY_RATIO_NODE_U_3RD_QUARTILE] = third_q
        df[c.DEMAND_CAPACITY_RATIO_NODE_U_4TH_QUARTILE] = fourth_q
        
        
        quartile = q.Quartile(self.demand_capacity_ratio_node_v)
        
        first_q, second_q, third_q, fourth_q = quartile.calc_quartiles()   
        
        df[c.DEMAND_CAPACITY_RATIO_NODE_V_1ST_QUARTILE] = first_q
        df[c.DEMAND_CAPACITY_RATIO_NODE_V_2ND_QUARTILE] = second_q
        df[c.DEMAND_CAPACITY_RATIO_NODE_V_3RD_QUARTILE] = third_q
        df[c.DEMAND_CAPACITY_RATIO_NODE_V_4TH_QUARTILE] = fourth_q
        
        df[c.U_NODE_DEMAND_CAPACITY_RATIO] = self.demand_capacity_ratio_node_u
        df[c.V_NODE_DEMAND_CAPACITY_RATIO] = self.demand_capacity_ratio_node_v