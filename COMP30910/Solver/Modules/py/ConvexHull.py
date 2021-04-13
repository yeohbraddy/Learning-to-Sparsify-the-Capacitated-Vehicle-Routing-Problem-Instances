import Constants as c, Quartile as q, Graph as g
from scipy.spatial import ConvexHull
import numpy as np

import time


class CHull:
    def __init__(self, points, num_of_nodes):
        self.hull = ConvexHull(points)
        self.num_of_nodes = num_of_nodes
        self.node_u_euc_distance_to_nearest_convex_hull_vertex = []
        self.node_v_euc_distance_to_nearest_convex_hull_vertex = []
        self.convex_hull_edge_length = []
        
    def calc_euc_distance(self, lst_a, lst_b):
        a = np.array(lst_a)
        b = np.array(lst_b)
        norm = np.linalg.norm(a-b)
        
        return norm
    
    def calc_min_distance(self, node0):
        min_dist = 100000000
            
        for v in self.hull.vertices:
            node1 = self.hull.points[v]

            dist = g.calculate_weight(node0, node1)
            if dist < min_dist:
                min_dist = dist
                
        return min_dist
    
    def get_idx_of_ch_vertex(self, node):
        arr = np.unique(np.where(self.hull.points == node)[0])
        for v in self.hull.vertices:
            start = 0 
            end = len(arr) - 1
            
            while start <= end:
                mid = start + (end - start) // 2
                idx = arr[mid]
                
                if idx < v:
                    start = mid + 1
                elif idx > v:
                    end = mid - 1
                else:
                    return idx
                    break
                    
        return -1
        
    def add_convex_hull_features(self, node_u, node_v, weight):
        pos = self.get_idx_of_ch_vertex(node_u)

        if pos in self.hull.vertices:
            min_dist = self.calc_min_distance(node_u)
                
            self.node_u_euc_distance_to_nearest_convex_hull_vertex.append(min_dist / self.num_of_nodes)
        else:
            self.node_u_euc_distance_to_nearest_convex_hull_vertex.append(0)
   

        pos = self.get_idx_of_ch_vertex(node_v)
            
        if pos in self.hull.vertices:
            min_dist = self.calc_min_distance(node_v)
                
            self.node_v_euc_distance_to_nearest_convex_hull_vertex.append(min_dist / self.num_of_nodes)
        else:
            self.node_v_euc_distance_to_nearest_convex_hull_vertex.append(0)
        
        pos0 = self.get_idx_of_ch_vertex(node_u)
        pos1 = self.get_idx_of_ch_vertex(node_v)
           
        if pos0 in self.hull.vertices and pos1 in self.hull.vertices:
            self.convex_hull_edge_length.append(weight)
        else:
            self.convex_hull_edge_length.append(0)

    def add_to_df(self, df):       
        df[c.NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX] = self.node_u_euc_distance_to_nearest_convex_hull_vertex
        df[c.NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX] = self.node_v_euc_distance_to_nearest_convex_hull_vertex
        df[c.CONVEX_HULL_EDGE_LENGTH] = self.convex_hull_edge_length
        
        