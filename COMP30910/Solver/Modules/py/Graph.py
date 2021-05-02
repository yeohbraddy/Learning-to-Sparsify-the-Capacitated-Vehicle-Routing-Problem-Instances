#!/usr/bin/env python
# coding: utf-8

import Constants as c
import numpy as np
import pandas as pd
import matplotlib as plt
import networkx as nx
from collections import defaultdict
import time

# Helper functions to generate a dataframe containing the edges and its relative information.
# It also creates a graph that enables to calculate more features.

def compare_coord_id(u, v):
    return u == v

def check_edge_exists(tempSet, str1, str2):
    return str1 in tempSet or str2 in tempSet

# We want to check if a certain edge exists if an arbitrary set, so we build
# unique strings and store it
def string_edge_builder(u, v):
    return "(" + u + ", " + v + ")"

def create_edge_strings(u, v):
    return string_edge_builder(u, v), string_edge_builder(v, u)

def calculate_weight(coord_u, coord_v):
    a = np.array(coord_u)
    b = np.array(coord_v)
    return np.linalg.norm(a - b)

def is_depot(node):
    return node == "1"

def get_edges_in_optimal_route(routes):
    edges_in_optimal_route = set()
    for route in routes:
        curr = routes[route]

        for index in range(0, len(curr) - 1):
            coord_str1, coord_str2 = create_edge_strings(
                curr[index], curr[index + 1])

#             if not check_edge_exists(edges_in_optimal_route, coord_str1, coord_str2):
            edges_in_optimal_route.add(coord_str1)
            edges_in_optimal_route.add(coord_str2)
    return edges_in_optimal_route

def init_incident_matrix(coords, matrix_size):
    arr = np.zeros((matrix_size, matrix_size))
    return label_matrix(coords, arr)

def label_matrix(coords, arr):
    row_labels = [row for row in coords]
    column_labels = [col for col in coords]
    incidence_matrix = pd.DataFrame(
        arr, columns=column_labels, index=row_labels)

    return incidence_matrix

# Creating a dataframe where each row is an edge containing features extracted from the instance file.
# This dataframe serves as the core of the data for the machine learning and also allows us to compute other features.
def create_edges_df(coords, routes, file_name, demand, capacity, num_of_vehicles, num_of_nodes):
    edges_in_optimal_route = get_edges_in_optimal_route(routes)
    # Calculates local edge rank by creating a distance matrix
    incidence_matrix = init_incident_matrix(coords, len(coords))
    edges_dict = defaultdict(list)
    dict_global_edge_rank = {}
    index = 0
    num_of_nodes = int(num_of_nodes)
    dbscan = []

    for u, coord_u in coords.items():
        for v, coord_v in coords.items():
            if not compare_coord_id(u, v):
                coord_str1, coord_str2 = string_edge_builder(u, v), string_edge_builder(v, u)

                edge_weight = calculate_weight(coord_u, coord_v) / num_of_nodes
         
                dbscan.append([coord_u[0], coord_u[1]])

                edges_dict[c.U_X].append(coord_u[0])
                edges_dict[c.U_Y].append(coord_u[1])
                edges_dict[c.U_NODE_ID].append(u)

                dbscan.append([coord_v[0], coord_v[1]])

                edges_dict[c.V_X].append(coord_v[0])
                edges_dict[c.V_Y].append(coord_v[1])
                edges_dict[c.V_NODE_ID].append(v)

                edges_dict[c.FILE_NAME].append(file_name)
                edges_dict[c.U_NODE_DEMAND].append(demand[int(u)] / num_of_nodes)
                edges_dict[c.V_NODE_DEMAND].append(demand[int(v)] / num_of_nodes)

                edges_dict[c.EDGE_WEIGHT].append(edge_weight)
                # For networkx graph weights
                edges_dict[c.EDGE_WEIGHT_NON_NORMALISED].append(edge_weight * num_of_nodes)
                dict_global_edge_rank[index] = edge_weight
                index += 1

                if check_edge_exists(edges_in_optimal_route, coord_str1, coord_str2):
                    edges_dict[c.IS_OPTIMAL_EDGE].append(1)
                else:
                    edges_dict[c.IS_OPTIMAL_EDGE].append(0)

                if is_depot(u):
                    edges_dict[c.IS_NODE_U_DEPOT].append(1)
                    edges_dict[c.IS_NODE_V_DEPOT].append(0)
                elif is_depot(v):
                    edges_dict[c.IS_NODE_U_DEPOT].append(0)
                    edges_dict[c.IS_NODE_V_DEPOT].append(1)
                else:
                    edges_dict[c.IS_NODE_U_DEPOT].append(0)
                    edges_dict[c.IS_NODE_V_DEPOT].append(0)
                incidence_matrix[str(u)][str(v)] = edge_weight 
    return pd.DataFrame(edges_dict), dict_global_edge_rank, incidence_matrix, dbscan


def build_graph(df, is_optimal_edges_only=False):
    plt.rcParams["figure.figsize"] = [16, 9]

    if is_optimal_edges_only:
        graph = df[[c.U_NODE_ID, c.V_NODE_ID]].where(
            df[c.IS_OPTIMAL_EDGE] == 1)
    else:
        graph = df[[c.U_NODE_ID, c.V_NODE_ID, c.EDGE_WEIGHT_NON_NORMALISED]]

    G = nx.from_pandas_edgelist(graph, c.U_NODE_ID, c.V_NODE_ID, edge_attr=c.EDGE_WEIGHT_NON_NORMALISED)

    return G


def plot_graph(G):
    nx.draw(G, with_labels=True)
    plt.show()
