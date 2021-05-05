#!/usr/bin/env python
# coding: utf-8

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
import TwoIndexSolver as solver
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

base_path = os.getcwd() + "/Instances"
instances_path = base_path + "/Instances/"
solutions_path = base_path + "/Solutions/"
instances_prune_path = base_path + "/Instances - Prune/"
solutions_prune_path = base_path + "/Solutions - Prune/"

instances_files = [f for f in listdir(
    instances_path) if isfile(join(instances_path, f))]
solutions_files = [f for f in listdir(
    solutions_path) if isfile(join(solutions_path, f))]
instances_prune_files = [f for f in listdir(
    instances_prune_path) if isfile(join(instances_prune_path, f))]
solutions_prune_files = [f for f in listdir(
    solutions_prune_path) if isfile(join(solutions_prune_path, f))]

# Script to perform feature computation on the instances

def generate_features(is_prune):
    
    df = pd.DataFrame(columns = c.column_names)
    
    is_prune = is_prune

    # Getting path of the files
    instances = instances_prune_files if is_prune else instances_files
    solutions = solutions_prune_files if is_prune else solutions_files
    
    i_path = instances_prune_path if is_prune else instances_path
    s_path = solutions_prune_path if is_prune else solutions_path
    
    # Going through each instance we want to generate features for
    for index in range(0, len(instances)):
        instance_file = instances[index]

        # Q = capacity
        # q = demand
        # p = number of vehicles

        # Reading in the variables of the instance
        xc, yc, coords, q, Q, p, n, coords_node_id_dict = fp.read_instance(
            i_path + instance_file)
        
        # +1 because it returns number of customers and not number of nodes
        n += 1
        
        # Reading its respective solution
        routes = fp.read_solution(s_path + solutions[index])
        
        # If there are multiple unique solutions, this generates features for the optimal edges that have have not been encountered
        # This is not used as we verified there are no multiple unique solutions.
        # This function was used to verify. In the future, if there are multiple solutions, this function may be used.
#         for idx in range(0, len(solutions)):
#             engineered_solution = solutions[idx] 
#             temp0 = instance_file[:len(instance_file) - 4] + "-" + str(idx) + "-solution.txt"
#             temp1 = instance_file[:len(instance_file) - 4] + "-solution.txt"
            
#             if temp0 == engineered_solution or temp1 == engineered_solution:
#                 routes = fp.read_solution(e_path + engineered_solution)

#                 optimal_edge = g.get_edges_in_optimal_route(routes)
                
#                 edges_in_optimal_route = edges_in_optimal_route | optimal_edge
                

        # Computing features relating to the MILP problem
        lp_relaxation, reduced_cost, active_arcs, objective_value = solver.solve(
            i_path + instance_file, "", is_binary=False, enable_logging=False, is_pruned=False)

        # Generating the core dataframe of edges and the features extracted from the instance file
        edges_df, dict_global_edge_rank, incidence_matrix, dbscan = g.create_edges_df(
            coords, routes, instance_file, q, Q, p, n)

        # Objects to compute more features
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

        # For each edge of the problem instance
        for index, row in edges_df.iterrows():
            node_u, node_v = row[c.U_NODE_ID], row[c.V_NODE_ID]
            weight = row[c.EDGE_WEIGHT]
            u_x, u_y = row[c.U_X], row[c.U_Y]
            v_x, v_y = row[c.V_X], row[c.V_Y]

            # Compute features
            globalEdgeRank.add_ranking(weight)
            localEdgeRank.add_rankings(node_u, node_v)
            LPR.add_relaxation(node_u, node_v)
            ratio.add_ratios(node_u, node_v)
            RC.add_reduced_cost(node_u, node_v)
            DBS.add_dbscan((u_x, u_y), (v_x, v_y))
            CH.add_convex_hull_features([u_x, u_y], [v_x, v_y], weight)
            D.add_distance_features([u_x, u_y], [v_x, v_y])

        # Add to the dataframe
        for o in objs:
            o.add_to_df(edges_df)

        # Concatenate it with the main dataframe which consists of all the instances computed so far
        frames = [df, edges_df]
        df = pd.concat(frames, ignore_index=True)


    path = os.getcwd() + "\Data\\"
    if is_prune:
        df.to_csv(path + 'data_prune.csv', index=True)
    else:
        df.to_csv(path + 'data.csv', index=True)


