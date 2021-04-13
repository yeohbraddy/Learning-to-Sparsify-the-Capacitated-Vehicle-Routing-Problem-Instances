import Constants as c, Graph as g
import numpy as np

class Distance:
    def __init__(self, coords, num_of_nodes):
        self.coords = coords
        self.num_of_nodes = num_of_nodes
        self.centroid = self.calculate_centroid()
        self.node_u_dist_to_centroid = []
        self.node_v_dist_to_centroid = []
        self.node_average_dist_to_centroid = []
        self.depot = coords['1']
        self.node_u_distance_to_depot = []
        self.node_v_distance_to_depot = []
        self.node_average_distance_to_depot = []
        self.angle_degree_to_depot = []
        self.node_u_dist_to_nearest_neighbour = []
        self.node_v_dist_to_nearest_neighbour = []
        self.node_average_dist_to_nearest_neighbour = []
        
        
    def calculate_centroid(self):
        arr = list(self.coords.values())
        
        sum_x = 0
        sum_y = 0
        for a in arr:
            sum_x += a[0]
            sum_y += a[1]
        
        length = len(arr[0])
        
        return [sum_x / length, sum_y / length]
        
    def add_centroid_distance(self, node_u, node_v):
        dist_u = g.calculate_weight(self.centroid, node_u)
        self.node_u_dist_to_centroid.append(dist_u / self.num_of_nodes)
        
        dist_v = g.calculate_weight(self.centroid, node_v)
        self.node_v_dist_to_centroid.append(dist_v / self.num_of_nodes)
        
        self.node_average_dist_to_centroid.append((dist_u + dist_v) / 2)
        
    def add_distance_to_depot(self, node_u, node_v):
        dist_u = g.calculate_weight(self.depot, node_u)
        self.node_u_distance_to_depot.append(dist_u / self.num_of_nodes)
        
        dist_v = g.calculate_weight(self.depot, node_v)
        self.node_v_distance_to_depot.append(dist_v / self.num_of_nodes)
        
        self.node_average_distance_to_depot.append((dist_u + dist_v) / 2)
     
    def add_angle_degree_to_depot(self, node_u, node_v):
        if node_u == self.depot or node_v == self.depot:
            self.angle_degree_to_depot.append(0)
        else:
            points = np.array([self.depot, node_u, node_v])
            A = points[1] - points[0]
            B = points[2] - points[1]
            C = points[0] - points[2]

            angles = []
            for e1, e2 in ((A, -B), (B, -C), (C, -A)):
                num = np.dot(e1, e2)
                denom = np.linalg.norm(e1) * np.linalg.norm(e2)
                angles.append(np.arccos(round(num/denom, 5)) * 180 / np.pi)
                

            self.angle_degree_to_depot.append(angles[0])
        
        
    def calc_min_dist(self, node):
        min_dist = 100000
        
        for n in list(self.coords.values()):
            dist = g.calculate_weight(node, n)
            
            if dist < min_dist:
                min_dist = dist
                
        return min_dist
        
    def add_nearest_neighbour_distance(self, node_u, node_v):
        dist0 = self.calc_min_dist(node_u)
        self.node_u_dist_to_nearest_neighbour.append(dist0 / self.num_of_nodes)
        
        dist1 = self.calc_min_dist(node_v)
        self.node_v_dist_to_nearest_neighbour.append(dist1 / self.num_of_nodes)

        self.node_average_dist_to_nearest_neighbour.append((dist0 + dist1) / 2)
    
        
    def add_distance_features(self, node_u, node_v):
        self.add_centroid_distance(node_u, node_v)
        self.add_distance_to_depot(node_u, node_v)
        self.add_angle_degree_to_depot(node_u, node_v)
        self.add_nearest_neighbour_distance(node_u, node_v)
        
    def add_to_df(self, df):
        df[c.NODE_U_DIST_TO_CENTROID] = self.node_u_dist_to_centroid
        df[c.NODE_V_DIST_TO_CENTROID] = self.node_v_dist_to_centroid
        df[c.NODE_AVERAGE_DIST_TO_CENTROID] = self.node_average_dist_to_centroid
        
        df[c.NODE_U_DIST_TO_DEPOT] = self.node_u_distance_to_depot
        df[c.NODE_V_DIST_TO_DEPOT] = self.node_v_distance_to_depot
        df[c.NODE_AVERAGE_DIST_TO_DEPOT] = self.node_average_distance_to_depot
        
        df[c.ANGLE_DEGREE_TO_DEPOT] = self.angle_degree_to_depot
        
        df[c.NODE_U_DIST_TO_NEAREST_NEIGHBOUR] = self.node_u_dist_to_nearest_neighbour
        df[c.NODE_V_DIST_TO_NEAREST_NEIGHBOUR] = self.node_v_dist_to_nearest_neighbour
        df[c.NODE_AVERAGE_DIST_TO_NEAREST_NEIGHBOUR] = self.node_average_dist_to_nearest_neighbour
        
        return df
        