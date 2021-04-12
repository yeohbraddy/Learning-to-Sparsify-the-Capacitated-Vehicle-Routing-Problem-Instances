import Constants as c
import networkx as nx

class Centrality:
    def __init__(self, G, num_of_nodes):
        self.closeness_centrality = nx.closeness_centrality(G, distance=c.EDGE_WEIGHT_NON_NORMALISED)
        self.num_of_nodes = num_of_nodes
        self.node_u_closeness_centrality = []
        self.node_v_closeness_centrality = []
        self.node_average_closeness_centrality = []
        self.current_flow_betweenness_centrality = nx.current_flow_betweenness_centrality(G, weight=c.EDGE_WEIGHT_NON_NORMALISED)
        self.node_u_current_flow_betweenness_centrality = []
        self.node_v_current_flow_betweenness_centrality = []
        self.node_average_current_flow_betweenness_centrality = []
        self.ecfbc = nx.edge_current_flow_betweenness_centrality(G, weight=c.EDGE_WEIGHT_NON_NORMALISED)
        self.edge_current_flow_betweenness_centrality = []
                
    def add_centrality_features(self, node_u, node_v):
        node_u_closeness_centrality = self.closeness_centrality[node_u] / self.num_of_nodes
        self.node_u_closeness_centrality.append(node_u_closeness_centrality)
        
        node_v_closeness_centrality = self.closeness_centrality[node_v] / self.num_of_nodes
        self.node_v_closeness_centrality.append(node_v_closeness_centrality)
        
        self.node_average_closeness_centrality.append((node_u_closeness_centrality + node_v_closeness_centrality) / 2)
        
        
        node_u_current_flow_betweenness_centrality = self.current_flow_betweenness_centrality[node_u] / self.num_of_nodes
        self.node_u_current_flow_betweenness_centrality.append(node_u_current_flow_betweenness_centrality)
        
        node_v_current_flow_betweenness_centrality = self.current_flow_betweenness_centrality[node_v] / self.num_of_nodes
        self.node_v_current_flow_betweenness_centrality.append(node_v_current_flow_betweenness_centrality)
        
        self.node_average_current_flow_betweenness_centrality.append((node_u_current_flow_betweenness_centrality + node_v_current_flow_betweenness_centrality) / 2)
        
        num = 0
        if (node_u, node_v) in self.ecfbc:
            num = self.ecfbc[(node_u, node_v)]
        else:
            num = self.ecfbc[(node_v, node_u)]
            
        self.edge_current_flow_betweenness_centrality.append(num / self.num_of_nodes)
     
        
    def add_to_df(self, df):
        df[c.NODE_U_CLOSENESS_CENTRALITY] = self.node_u_closeness_centrality
        df[c.NODE_V_CLOSENESS_CENTRALITY] = self.node_v_closeness_centrality
        df[c.NODE_AVERAGE_CLOSENESS_CENTRALITY] = self.node_average_closeness_centrality
        
        df[c.NODE_U_CURRENT_FLOW_BETWEENESS_CENTRALITY] = self.node_u_current_flow_betweenness_centrality
        df[c.NODE_V_CURRENT_FLOW_BETWEENESS_CENTRALITY] = self.node_v_current_flow_betweenness_centrality
        df[c.NODE_AVERAGE_CURRENT_FLOW_BETWEENESS_CENTRALITY] = self.node_average_current_flow_betweenness_centrality
        
        df[c.EDGE_CURRENT_FLOW_BETWEENESS_CENTRALITY] = self.edge_current_flow_betweenness_centrality
        
        return df