#!/usr/bin/env python
# coding: utf-8

# ### Feature names

# In[2]:


U_NODE_ID = "U_NODE_ID"
V_NODE_ID = "V_NODE_ID"

U_X = "U_X"
U_Y = "U_Y"

V_X = "V_X"
V_Y = "V_Y"

IS_NODE_U_DEPOT = "IS_NODE_U_DEPOT"
IS_NODE_V_DEPOT = "IS_NODE_V_DEPOT"

IS_OPTIMAL_EDGE = "IS_OPTIMAL_EDGE"
EDGE_WEIGHT = "EDGE_WEIGHT"

GLOBAL_RANK = "GLOBAL_RANK"
U_NODE_LOCAL_EDGE_RANK = "U_NODE_LOCAL_EDGE_RANK"
V_NODE_LOCAL_EDGE_RANK = "V_NODE_LOCAL_EDGE_RANK"

U_NODE_DEGREE = "U_NODE_DEGREE"
V_NODE_DEGREE = "V_NODE_DEGREE"
AVERAGE_NODE_DEGREE = "AVERAGE_NODE_DEGREE"

U_NODE_CLUSTERING = "U_NODE_CLUSTERING"
V_NODE_CLUSTERING = "V_NODE_CLUSTERING"
AVERAGE_NODE_CLUSTERING = "AVERAGE_NODE_CLUSTERING"

IS_MST_EDGE = "IS_MST_EDGE"
MST_WEIGHT = "MST_WEIGHT"
MST_U_DEGREE = "MST_U_DEGREE"
MST_V_DEGREE = "MST_V_DEGREE"

LP_RELAXATION = "LP_RELAXATION"

FILE_NAME = "FILE_NAME"
U_NODE_DEMAND = "U_NODE_DEMAND"
V_NODE_DEMAND = "V_NODE_DEMAND"
CAPACITY = "CAPACITY"
NUM_OF_VEHICLES = "NUM_OF_VEHICLES"

U_NODE_DEMAND_CAPACITY_RATIO = "U_NODE_DEMAND_CAPACITY_RATIO"
V_NODE_DEMAND_CAPACITY_RATIO = "V_NODE_DEMAND_CAPACITY_RATIO"

REDUCED_COST = "REDUCED_COST"

U_NODE_DBSCAN = "U_NODE_DBSCAN"
V_NODE_DBSCAN = "V_NODE_DBSCAN"
AVERAGE_NODE_DBSCAN = "AVERAGE_NODE_DBSCAN"

U_NODE_DEGREE_1ST_QUARTILE = "U_NODE_DEGREE_1ST_QUARTILE"
U_NODE_DEGREE_2ND_QUARTILE = "U_NODE_DEGREE_2ND_QUARTILE"
U_NODE_DEGREE_3RD_QUARTILE = "U_NODE_DEGREE_3RD_QUARTILE"
U_NODE_DEGREE_4TH_QUARTILE = "U_NODE_DEGREE_4TH_QUARTILE"
V_NODE_DEGREE_1ST_QUARTILE = "V_NODE_DEGREE_1ST_QUARTILE"
V_NODE_DEGREE_2ND_QUARTILE = "V_NODE_DEGREE_2ND_QUARTILE"
V_NODE_DEGREE_3RD_QUARTILE = "V_NODE_DEGREE_3RD_QUARTILE"
V_NODE_DEGREE_4TH_QUARTILE = "V_NODE_DEGREE_4TH_QUARTILE"

U_NODE_DBSCAN_1ST_QUARTILE = "U_NODE_DBSCAN_1ST_QUARTILE"
U_NODE_DBSCAN_2ND_QUARTILE = "U_NODE_DBSCAN_2ND_QUARTILE"
U_NODE_DBSCAN_3RD_QUARTILE = "U_NODE_DBSCAN_3RD_QUARTILE"
U_NODE_DBSCAN_4TH_QUARTILE = "U_NODE_DBSCAN_4TH_QUARTILE"
V_NODE_DBSCAN_1ST_QUARTILE = "V_NODE_DBSCAN_1ST_QUARTILE"
V_NODE_DBSCAN_2ND_QUARTILE = "V_NODE_DBSCAN_2ND_QUARTILE"
V_NODE_DBSCAN_3RD_QUARTILE = "V_NODE_DBSCAN_3RD_QUARTILE"
V_NODE_DBSCAN_4TH_QUARTILE = "V_NODE_DBSCAN_4TH_QUARTILE"

U_NODE_CLUSTERING_1ST_QUARTILE = "U_NODE_CLUSTERING_1ST_QUARTILE"
U_NODE_CLUSTERING_2ND_QUARTILE = "U_NODE_CLUSTERING_2ND_QUARTILE"
U_NODE_CLUSTERING_3RD_QUARTILE = "U_NODE_CLUSTERING_3RD_QUARTILE"
U_NODE_CLUSTERING_4TH_QUARTILE = "U_NODE_CLUSTERING_4TH_QUARTILE"
V_NODE_CLUSTERING_1ST_QUARTILE = "V_NODE_CLUSTERING_1ST_QUARTILE"
V_NODE_CLUSTERING_2ND_QUARTILE = "V_NODE_CLUSTERING_2ND_QUARTILE"
V_NODE_CLUSTERING_3RD_QUARTILE = "V_NODE_CLUSTERING_3RD_QUARTILE"
V_NODE_CLUSTERING_4TH_QUARTILE = "V_NODE_CLUSTERING_4TH_QUARTILE"

GLOBAL_EDGE_RANK_1ST_QUARTILE = "GLOBAL_EDGE_RANK_1ST_QUARTILE"
GLOBAL_EDGE_RANK_2ND_QUARTILE = "GLOBAL_EDGE_RANK_2ND_QUARTILE"
GLOBAL_EDGE_RANK_3RD_QUARTILE = "GLOBAL_EDGE_RANK_3RD_QUARTILE"
GLOBAL_EDGE_RANK_4TH_QUARTILE = "GLOBAL_EDGE_RANK_4TH_QUARTILE"

U_NODE_LOCAL_EDGE_RANK_1ST_QUARTILE = "U_NODE_LOCAL_EDGE_RANK_1ST_QUARTILE"
U_NODE_LOCAL_EDGE_RANK_2ND_QUARTILE = "U_NODE_LOCAL_EDGE_RANK_2ND_QUARTILE"
U_NODE_LOCAL_EDGE_RANK_3RD_QUARTILE = "U_NODE_LOCAL_EDGE_RANK_3RD_QUARTILE"
U_NODE_LOCAL_EDGE_RANK_4TH_QUARTILE = "U_NODE_LOCAL_EDGE_RANK_4TH_QUARTILE"
V_NODE_LOCAL_EDGE_RANK_1ST_QUARTILE = "V_NODE_LOCAL_EDGE_RANK_1ST_QUARTILE"
V_NODE_LOCAL_EDGE_RANK_2ND_QUARTILE = "V_NODE_LOCAL_EDGE_RANK_2ND_QUARTILE"
V_NODE_LOCAL_EDGE_RANK_3RD_QUARTILE = "V_NODE_LOCAL_EDGE_RANK_3RD_QUARTILE"
V_NODE_LOCAL_EDGE_RANK_4TH_QUARTILE = "V_NODE_LOCAL_EDGE_RANK_4TH_QUARTILE"

LP_RELAXATION_1ST_QUARTILE = "LP_RELAXATION_1ST_QUARTILE"
LP_RELAXATION_2ND_QUARTILE = "LP_RELAXATION_2ND_QUARTILE"
LP_RELAXATION_3RD_QUARTILE = "LP_RELAXATION_3RD_QUARTILE"
LP_RELAXATION_4TH_QUARTILE = "LP_RELAXATION_4TH_QUARTILE"

MST_U_DEGREE_1ST_QUARTILE = "MST_U_DEGREE_1ST_QUARTILE"
MST_U_DEGREE_2ND_QUARTILE = "MST_U_DEGREE_2ND_QUARTILE"
MST_U_DEGREE_3RD_QUARTILE = "MST_U_DEGREE_3RD_QUARTILE"
MST_U_DEGREE_4TH_QUARTILE = "MST_U_DEGREE_4TH_QUARTILE"
MST_V_DEGREE_1ST_QUARTILE = "MST_V_DEGREE_1ST_QUARTILE"
MST_V_DEGREE_2ND_QUARTILE = "MST_V_DEGREE_2ND_QUARTILE"
MST_V_DEGREE_3RD_QUARTILE = "MST_V_DEGREE_3RD_QUARTILE"
MST_V_DEGREE_4TH_QUARTILE = "MST_V_DEGREE_4TH_QUARTILE"

MST_WEIGHT_1ST_QUARTILE = "MST_WEIGHT_1ST_QUARTILE"
MST_WEIGHT_2ND_QUARTILE = "MST_WEIGHT_2ND_QUARTILE"
MST_WEIGHT_3RD_QUARTILE = "MST_WEIGHT_3RD_QUARTILE"
MST_WEIGHT_4TH_QUARTILE = "MST_WEIGHT_4TH_QUARTILE"

DEMAND_CAPACITY_RATIO_NODE_U_1ST_QUARTILE = "DEMAND_CAPACITY_RATIO_NODE_U_1ST_QUARTILE"
DEMAND_CAPACITY_RATIO_NODE_U_2ND_QUARTILE = "DEMAND_CAPACITY_RATIO_NODE_U_2ND_QUARTILE"
DEMAND_CAPACITY_RATIO_NODE_U_3RD_QUARTILE = "DEMAND_CAPACITY_RATIO_NODE_U_3RD_QUARTILE"
DEMAND_CAPACITY_RATIO_NODE_U_4TH_QUARTILE = "DEMAND_CAPACITY_RATIO_NODE_U_4TH_QUARTILE"
DEMAND_CAPACITY_RATIO_NODE_V_1ST_QUARTILE = "DEMAND_CAPACITY_RATIO_NODE_V_1ST_QUARTILE"
DEMAND_CAPACITY_RATIO_NODE_V_2ND_QUARTILE = "DEMAND_CAPACITY_RATIO_NODE_V_2ND_QUARTILE"
DEMAND_CAPACITY_RATIO_NODE_V_3RD_QUARTILE = "DEMAND_CAPACITY_RATIO_NODE_V_3RD_QUARTILE"
DEMAND_CAPACITY_RATIO_NODE_V_4TH_QUARTILE = "DEMAND_CAPACITY_RATIO_NODE_V_4TH_QUARTILE"

REDUCED_COST_1ST_QUARTILE = "REDUCED_COST_1ST_QUARTILE"
REDUCED_COST_2ND_QUARTILE = "REDUCED_COST_2ND_QUARTILE"
REDUCED_COST_3RD_QUARTILE = "REDUCED_COST_3RD_QUARTILE"
REDUCED_COST_4TH_QUARTILE = "REDUCED_COST_4TH_QUARTILE"

NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_1ST_QUARTILE = "NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_1ST_QUARTILE"
NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_2ND_QUARTILE = "NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_2ND_QUARTILE"
NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_3RD_QUARTILE = "NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_3RD_QUARTILE"
NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_4TH_QUARTILE = "NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_4TH_QUARTILE"
NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_1ST_QUARTILE = "NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_1ST_QUARTILE"
NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_2ND_QUARTILE = "NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_2ND_QUARTILE"
NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_3RD_QUARTILE = "NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_3RD_QUARTILE"
NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_4TH_QUARTILE = "NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX_4TH_QUARTILE"

CONVEX_HULL_EDGE_LENGTH_1ST_QUARTILE = "CONVEX_HULL_EDGE_LENGTH_1ST_QUARTILE"
CONVEX_HULL_EDGE_LENGTH_2ND_QUARTILE = "CONVEX_HULL_EDGE_LENGTH_2ND_QUARTILE"
CONVEX_HULL_EDGE_LENGTH_3RD_QUARTILE = "CONVEX_HULL_EDGE_LENGTH_3RD_QUARTILE"
CONVEX_HULL_EDGE_LENGTH_4TH_QUARTILE = "CONVEX_HULL_EDGE_LENGTH_4TH_QUARTILE"

NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX = "NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX"
NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX = "NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX"
CONVEX_HULL_EDGE_LENGTH = "CONVEX_HULL_EDGE_LENGTH"

NODE_U_EDGE_TRIANGLE_MULTIPLICITY = "NODE_U_EDGE_TRIANGLE_MULTIPLICITY"
NODE_V_EDGE_TRIANGLE_MULTIPLICITY = "NODE_V_EDGE_TRIANGLE_MULTIPLICITY"
NODE_AVERAGE_EDGE_TRIANGLE_MULTIPLICITY = "NODE_AVERAGE_EDGE_TRIANGLE_MULTIPLICITY"

NODE_U_EDGE_GENERALISED_DEGREE = "NODE_U_EDGE_GENERALISED_DEGREE"
NODE_V_EDGE_GENERALISED_DEGREE = "NODE_V_EDGE_GENERALISED_DEGREE"
NODE_AVERAGE_EDGE_GENERALISED_DEGREE = "NODE_AVERAGE_EDGE_GENERALISED_DEGREE"

NODE_U_EDGE_TRIANGLE_MULTIPLICITY_1ST_QUARTILE = "NODE_U_EDGE_TRIANGLE_MULTIPLICITY_1ST_QUARTILE"
NODE_U_EDGE_TRIANGLE_MULTIPLICITY_2ND_QUARTILE = "NODE_U_EDGE_TRIANGLE_MULTIPLICITY_2ND_QUARTILE"
NODE_U_EDGE_TRIANGLE_MULTIPLICITY_3RD_QUARTILE = "NODE_U_EDGE_TRIANGLE_MULTIPLICITY_3RD_QUARTILE"
NODE_U_EDGE_TRIANGLE_MULTIPLICITY_4TH_QUARTILE = "NODE_U_EDGE_TRIANGLE_MULTIPLICITY_4TH_QUARTILE"

NODE_V_EDGE_TRIANGLE_MULTIPLICITY_1ST_QUARTILE = "NODE_V_EDGE_TRIANGLE_MULTIPLICITY_1ST_QUARTILE"
NODE_V_EDGE_TRIANGLE_MULTIPLICITY_2ND_QUARTILE = "NODE_V_EDGE_TRIANGLE_MULTIPLICITY_2ND_QUARTILE"
NODE_V_EDGE_TRIANGLE_MULTIPLICITY_3RD_QUARTILE = "NODE_V_EDGE_TRIANGLE_MULTIPLICITY_3RD_QUARTILE"
NODE_V_EDGE_TRIANGLE_MULTIPLICITY_4TH_QUARTILE = "NODE_V_EDGE_TRIANGLE_MULTIPLICITY_4TH_QUARTILE"

NODE_U_EDGE_GENERALISED_DEGREE_1ST_QUARTILE = "NODE_U_EDGE_GENERALISED_DEGREE_1ST_QUARTILE"
NODE_U_EDGE_GENERALISED_DEGREE_2ND_QUARTILE = "NODE_U_EDGE_GENERALISED_DEGREE_2ND_QUARTILE"
NODE_U_EDGE_GENERALISED_DEGREE_3RD_QUARTILE = "NODE_U_EDGE_GENERALISED_DEGREE_3RD_QUARTILE"
NODE_U_EDGE_GENERALISED_DEGREE_4TH_QUARTILE = "NODE_U_EDGE_GENERALISED_DEGREE_4TH_QUARTILE"

NODE_V_EDGE_GENERALISED_DEGREE_1ST_QUARTILE = "NODE_V_EDGE_GENERALISED_DEGREE_1ST_QUARTILE"
NODE_V_EDGE_GENERALISED_DEGREE_2ND_QUARTILE = "NODE_V_EDGE_GENERALISED_DEGREE_2ND_QUARTILE"
NODE_V_EDGE_GENERALISED_DEGREE_3RD_QUARTILE = "NODE_V_EDGE_GENERALISED_DEGREE_3RD_QUARTILE"
NODE_V_EDGE_GENERALISED_DEGREE_4TH_QUARTILE = "NODE_V_EDGE_GENERALISED_DEGREE_4TH_QUARTILE"

NODE_U_AVERAGE_DEGREE_CONNECTIVITY = "NODE_U_AVERAGE_DEGREE_CONNECTIVITY"
NODE_V_AVERAGE_DEGREE_CONNECTIVITY = "NODE_V_AVERAGE_DEGREE_CONNECTIVITY"
NODE_AVERAGE_AVERAGE_DEGREE_CONNECTIVITY = "NODE_AVERAGE_AVERAGE_DEGREE_CONNECTIVITY"

EDGE_WEIGHT_NON_NORMALISED = "EDGE_WEIGHT_NON_NORMALISED"

NODE_U_CLOSENESS_CENTRALITY = "NODE_U_CLOSENESS_CENTRALITY"
NODE_V_CLOSENESS_CENTRALITY = "NODE_V_CLOSENESS_CENTRALITY"
NODE_AVERAGE_CLOSENESS_CENTRALITY = "NODE_AVERAGE_CLOSENESS_CENTRALITY"

NODE_U_CURRENT_FLOW_BETWEENESS_CENTRALITY = "NODE_U_CURRENT_FLOW_BETWEENESS_CENTRALITY"
NODE_V_CURRENT_FLOW_BETWEENESS_CENTRALITY = "NODE_V_CURRENT_FLOW_BETWEENESS_CENTRALITY"
NODE_AVERAGE_CURRENT_FLOW_BETWEENESS_CENTRALITY = "NODE_AVERAGE_CURRENT_FLOW_BETWEENESS_CENTRALITY"

EDGE_CURRENT_FLOW_BETWEENESS_CENTRALITY = "EDGE_CURRENT_FLOW_BETWEENESS_CENTRALITY"

NODE_U_DIST_TO_CENTROID = "NODE_U_DIST_TO_CENTROID"
NODE_V_DIST_TO_CENTROID = "NODE_V_DIST_TO_CENTROID"
NODE_AVERAGE_DIST_TO_CENTROID = "NODE_AVERAGE_DIST_TO_CENTROID"

NODE_U_DIST_TO_DEPOT = "NODE_U_DIST_TO_DEPOT"
NODE_V_DIST_TO_DEPOT = "NODE_V_DIST_TO_DEPOT"
NODE_AVERAGE_DIST_TO_DEPOT = "NODE_AVERAGE_DIST_TO_DEPOT"

ANGLE_DEGREE_TO_DEPOT = "ANGLE_DEGREE_TO_DEPOT"

NODE_U_DIST_TO_NEAREST_NEIGHBOUR = "NODE_U_DIST_TO_NEAREST_NEIGHBOUR"
NODE_V_DIST_TO_NEAREST_NEIGHBOUR = "NODE_V_DIST_TO_NEAREST_NEIGHBOUR"
NODE_AVERAGE_DIST_TO_NEAREST_NEIGHBOUR = "NODE_AVERAGE_DIST_TO_NEAREST_NEIGHBOUR"
# In[3]:


column_names = [
    U_NODE_ID,
    V_NODE_ID,
    U_X,
    U_Y,
    V_X,
    V_Y,
    IS_NODE_U_DEPOT,
    IS_NODE_V_DEPOT,
    IS_OPTIMAL_EDGE,
    EDGE_WEIGHT,
    GLOBAL_RANK,
    U_NODE_LOCAL_EDGE_RANK,
    V_NODE_LOCAL_EDGE_RANK,
    LP_RELAXATION,
    FILE_NAME,
    U_NODE_DEMAND,
    V_NODE_DEMAND,
    U_NODE_DEMAND_CAPACITY_RATIO,
    V_NODE_DEMAND_CAPACITY_RATIO,
    REDUCED_COST,
    NODE_U_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX,
    NODE_V_EUC_DISTANCE_TO_NEAREST_CONVEX_HULL_VERTEX,
    CONVEX_HULL_EDGE_LENGTH,
    EDGE_WEIGHT_NON_NORMALISED,
    NODE_U_DIST_TO_CENTROID,
    NODE_V_DIST_TO_CENTROID,
    NODE_AVERAGE_DIST_TO_CENTROID,
    NODE_U_DIST_TO_DEPOT,
    NODE_V_DIST_TO_DEPOT,
    NODE_AVERAGE_DIST_TO_DEPOT
]


