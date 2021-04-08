import Constants as c, Quartile as q
from scipy.spatial import ConvexHull
import numpy as np

class CHull:
    def __init__(self, points, num_of_nodes):
        self.hull = ConvexHull(points)
        self.num_of_nodes = num_of_nodes
        self.node_u_euc_distance_to_nearest_convex_hull_vertex = []
        self.node_v_euc_distance_to_nearest_convex_hull_vertex = []
        self.convex_hull_edge_length = []
        
    def calc_euc_distance(self, a, b):
        return np.linalg.norm(a-b)
    
    def calc_min_distance(self, node0):
        min_dist = 0
            
        for v in self.hull.vertices:
            node1 = self.hull.points[v]

            dist = self.calc_euc_distance(node0, node1)
            if dist < min_dist:
                min_dist = dist
                
        return min_dist
    
    def get_idx_of_ch_vertex(self, node):
        return np.where(self.hull.points == node)[0]
        
    def add_convex_hull_features(self, node_u, node_v):
        pos = self.get_idx_of_ch_vertex(node_u)
            
        if pos in self.hull.vertices:
            node_u_euc_distance_to_nearest_convex_hull_vertex.append(0)
        else:
            min_dist = self.calc_min_distance(node_u)
                
            self.node_u_euc_distance_to_nearest_convex_hull_vertex.append(min_dist / self.num_of_nodes)
       
        pos = self.get_idx_of_ch_vertex(node_u)
            
        if pos in self.hull.vertices:
            node_v_euc_distance_to_nearest_convex_hull_vertex.append(0)
        else:
            min_dist = self.calc_min_distance(node_v)
                
            self.node_v_euc_distance_to_nearest_convex_hull_vertex.append(min_dist / self.num_of_nodes)
        
        pos0 = self.get_idx_of_ch_vertex(node_u)
        pos1 = self.get_idx_of_ch_vertex(node_v)
           
        if pos0 in self.hull.vertices and pos1 in self.hull.vertices:
            for idx in range(0, len(self.hull.vertices) - 1):
                if self.hull.vertices[idx] == pos0 and self.hull.vertices[idx + 1] == pos1:
                    dist = self.calc_euc_distance(node_u[0], node_u[1], node_v[0], node_v[1])
                    self.convex_hull_edge_length.append(dist / self.num_of_nodes)
                    break
        else:
            self.convex_hull_edge_length.append(0)

    def add_to_df(self, df):
        
        first_q, second_q, third_q, fourth_q = q.calc_quartiles(self.node_u_euc_distance_to_nearest_convex_hull_vertex, self.num_of_nodes)
        
        df[c.NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_1ST_QUARTILE] = first_q
        df[c.NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_2ND_QUARTILE] = second_q
        df[c.NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_3RD_QUARTILE] = third_q
        df[c.NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_4TH_QUARTILE] = fourth_q
        
        first_q, second_q, third_q, fourth_q = q.calc_quartiles(self.node_v_euc_distance_to_nearest_convex_hull_vertex, self.num_of_nodes)
        
        df[c.NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_1ST_QUARTILE] = first_q
        df[c.NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_2ND_QUARTILE] = second_q
        df[c.NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_3RD_QUARTILE] = third_q
        df[c.NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_4TH_QUARTILE] = fourth_q
        
        first_q, second_q, third_q, fourth_q = q.calc_quartiles(self.convex_hull_edge_length, self.num_of_nodes)
        
        df[c.CONVEX_HULL_EDGE_LENGTH_1ST_QUARTILE] = first_q
        df[c.CONVEX_HULL_EDGE_LENGTH_2ND_QUARTILE] = second_q
        df[c.CONVEX_HULL_EDGE_LENGTH_3RD_QUARTILE] = third_q
        df[c.CONVEX_HULL_EDGE_LENGTH_4TH_QUARTILE] = fourth_q
        
        df[c.NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX] = self.node_u_euc_distance_to_nearest_convex_hull_vertex
        df[c.NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX] = self.node_v_euc_distance_to_nearest_convex_hull_vertex
        df[c.CONVEX_HULL_EDGE_LENGTH] = self.convex_hull_edge_length
        
        