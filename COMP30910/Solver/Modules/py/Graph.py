#!/usr/bin/env python
# coding: utf-8

# In[6]:

import Constants as c
import numpy as np
import pandas as pd
import matplotlib as plt
import networkx as nx
from collections import defaultdict


# In[7]:


def compare_coord_id(u, v):
    return u == v


def check_edge_exists(tempSet, str1, str2):
    return str1 in tempSet or str2 in tempSet


def string_edge_builder(u, v):
    return "(" + u + ", " + v + ")"


def create_edge_strings(u, v):
    return string_edge_builder(u, v), string_edge_builder(v, u)


def calculate_weight(coord_u, coord_v):
#     return np.hypot(int(coord_u[0]) - int(coord_v[0]), int(coord_u[1]) - int(coord_v[1]))
    return np.linalg.norm(coord_u - coord_v)


def is_depot(u, v):
    return u == "1" or v == "1"


def get_edges_in_optimal_route(routes):
    edges_in_optimal_route = set()

    for route in routes:
        curr = routes[route]

        for index in range(0, len(curr) - 1):
            coord_str1, coord_str2 = create_edge_strings(
                curr[index], curr[index + 1])

            if not check_edge_exists(edges_in_optimal_route, coord_str1, coord_str2):
                edges_in_optimal_route.add(coord_str1)
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


def create_edges_df(coords, routes, file_name, demand, capacity, num_of_vehicles, num_of_nodes):
    edges_in_optimal_route = get_edges_in_optimal_route(routes)
    incidence_matrix = init_incident_matrix(coords, len(coords))
    edges_dict = defaultdict(list)
    edges_set = set()
    dict_global_edge_rank = {}
    index, row, column = 0, 1, 1
    num_of_nodes = int(num_of_nodes)
    
    dbscan = []

    for u, coord_u in coords.items():
        for v, coord_v in coords.items():
            coord_str1, coord_str2 = string_edge_builder(
                u, v), string_edge_builder(v, u)

            edge_weight = calculate_weight(coord_u, coord_v) / num_of_nodes
# and not check_edge_exists(edges_set, coord_str1, coord_str2)
            if not compare_coord_id(u, v):
                edges_set.add(coord_str1)

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
                edges_dict[c.CAPACITY].append(capacity / num_of_nodes)
                edges_dict[c.NUM_OF_VEHICLES].append(num_of_vehicles / num_of_nodes)

                edges_dict[c.EDGE_WEIGHT].append(edge_weight)
                edges_dict[c.EDGE_WEIGHT_NON_NORMALISED].append(edge_weight * num_of_nodes)
                dict_global_edge_rank[index] = edge_weight
                index += 1

                if check_edge_exists(edges_in_optimal_route, coord_str1, coord_str2):
                    edges_dict[c.IS_OPTIMAL_EDGE].append(1)
                else:
                    edges_dict[c.IS_OPTIMAL_EDGE].append(0)

                if is_depot(u, v):
                    edges_dict[c.IS_DEPOT].append(1)
                else:
                    edges_dict[c.IS_DEPOT].append(0)

            incidence_matrix[str(row)][str(column)] = edge_weight
            column += 1
        column = 0
        row += 1

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
# In[ ]:
