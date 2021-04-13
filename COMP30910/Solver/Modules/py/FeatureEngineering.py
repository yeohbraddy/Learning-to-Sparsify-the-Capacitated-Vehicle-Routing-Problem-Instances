#!/usr/bin/env python
# coding: utf-8

# ## Imports

# ### Python numerical modules

# In[1]:

import re
import sys
import os

from linecache import getline
from pathlib import Path
from os.path import isfile, join
from os import listdir

sys.path.append(str(Path(os.getcwd()).parent) + '\py')

import ReducedCost as rc
import Ratio as r
import LPRelaxation as lpr
import Solver as solver
import MinimumSpanningTree as mst
import Graph as g
import LocalEdgeRank as ler
import GlobalEdgeRank as ger
import FileParser as fp
import Degree as d
import Constants as c
import Clustering as cg
import DBScan as dbs
import ConvexHull as ch
import Centrality as cty
import Distance as distance

from gurobipy import Model, GRB, quicksum
import pandas as pd


# ### Python

# In[2]:





# ### Custom modules

# In[3]:


# ### Gurobi

# In[4]:


# ## Script to perform feature computation on the instances

# In[5]:

base_path = os.getcwd() + "/Instances"
instances_path = base_path + "/Instances/"
solutions_path = base_path + "/Solutions/"
instances_prune_path = base_path + "/Instances - Prune/"
solutions_prune_path = base_path + "/Solutions - Prune/"
solutions_engineered_path = base_path + "/Solutions - Engineered/"

instances_files = [f for f in listdir(
    instances_path) if isfile(join(instances_path, f))]
solutions_files = [f for f in listdir(
    solutions_path) if isfile(join(solutions_path, f))]
instances_prune_files = [f for f in listdir(
    instances_prune_path) if isfile(join(instances_prune_path, f))]
solutions_prune_files = [f for f in listdir(
    solutions_prune_path) if isfile(join(solutions_prune_path, f))]
engineered_solutions_files = [f for f in listdir(
    solutions_engineered_path) if isfile(join(solutions_engineered_path, f))]


# ### Q = capacity
# ### q = demand
# ### p = number of vehicles

# In[7]:

def generate_features(is_prune):
    
    df = pd.DataFrame(columns = c.column_names)
    
    is_prune = is_prune

    instances = instances_prune_files if is_prune else instances_files
    solutions = solutions_prune_files if is_prune else solutions_files
    engineered = engineered_solutions_files
    
    i_path = instances_prune_path if is_prune else instances_path
    s_path = solutions_prune_path if is_prune else solutions_path
    e_path = solutions_engineered_path
    
    for index in range(0, len(instances)):
        instance_file = instances[index]

        xc, yc, coords, q, Q, p, n, coords_node_id_dict = fp.read_instance(
            i_path + instance_file)
        
        n += 1
        
        edges_in_optimal_route = set()
        
        for idx in range(0, len(engineered)):
            engineered_solution = engineered[idx] 
            temp0 = instance_file[:len(instance_file) - 4] + "-" + str(idx) + "-solution.txt"
            temp1 = instance_file[:len(instance_file) - 4] + "-solution.txt"
            
            if temp0 == engineered_solution or temp1 == engineered_solution:
                routes = fp.read_solution(e_path + engineered_solution)

                optimal_edge = g.get_edges_in_optimal_route(routes)
                
                edges_in_optimal_route = edges_in_optimal_route | optimal_edge
                
            
        lp_relaxation, reduced_cost, active_arcs, objective_value = solver.solve(
            i_path + instance_file, "", is_binary=False, enable_logging=False, is_pruned=False)

        edges_df, dict_global_edge_rank, incidence_matrix, dbscan = g.create_edges_df(
            coords, edges_in_optimal_route, instance_file, q, Q, p, n)

        edges_in_optimal_route = edges_in_optimal_route

        DBS = dbs.DBScan(dbscan, n)
        G = g.build_graph(edges_df)
        globalEdgeRank = ger.GlobalEdgeRank(dict_global_edge_rank, n)
        localEdgeRank = ler.LocalEdgeRank(incidence_matrix, n)
        LPR = lpr.LPRelaxation(lp_relaxation, n)
        ratio = r.Ratio(q, Q, n)
        RC = rc.ReducedCost(reduced_cost, n)
        CH = ch.CHull(dbscan, n)
        D = distance.Distance(coords, n)

        objs = [
            DBS, 
            globalEdgeRank,
            localEdgeRank,
            LPR,
            ratio,
            RC,
            CH,
            D
       ]

        for index, row in edges_df.iterrows():
            node_u, node_v = row[c.U_NODE_ID], row[c.V_NODE_ID]
            weight = row[c.EDGE_WEIGHT]
            u_x, u_y = row[c.U_X], row[c.U_Y]
            v_x, v_y = row[c.V_X], row[c.V_Y]

            globalEdgeRank.add_ranking(weight)
            localEdgeRank.add_rankings(node_u, node_v)
            LPR.add_relaxation(node_u, node_v)
            ratio.add_ratios(node_u, node_v)
            RC.add_reduced_cost(node_u, node_v)
            DBS.add_dbscan((u_x, u_y), (v_x, v_y))
            CH.add_convex_hull_features([u_x, u_y], [v_x, v_y], weight)
            D.add_distance_features([u_x, u_y], [v_x, v_y])

        for o in objs:
            o.add_to_df(edges_df)


        frames = [df, edges_df]
        df = pd.concat(frames, ignore_index=True)


    # In[8]:

#     path = os.getcwd() + "\COMP30910\Solver\Data\\"
    path = os.getcwd() + "\Data\\"
    if is_prune:
        df.to_csv(path + 'data_prune.csv', index=True)
    else:
        df.to_csv(path + 'data.csv', index=True)


# In[ ]:
