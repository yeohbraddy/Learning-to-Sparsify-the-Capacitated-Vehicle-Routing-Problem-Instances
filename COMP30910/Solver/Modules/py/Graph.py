#!/usr/bin/env python
# coding: utf-8

# In[6]:


import Constants as c
import numpy as np
import pandas as pd
from collections import defaultdict
import matplotlib as plt
import networkx as nx



# In[7]:


def compareCoordID(u, v):
    return u == v

def checkEdgeExists(tempSet, str1, str2):
    return str1 in tempSet or str2 in tempSet

def stringEdgeBuilder(u, v):
    return "(" + u + ", " + v + ")"

def createEdgeStrings(u, v):
    return stringEdgeBuilder(u, v), stringEdgeBuilder(v, u)

def calculateWeight(coord_u, coord_v):
    return np.hypot(int(coord_u[0]) - int(coord_v[0]), int(coord_u[1]) - int(coord_v[1]))

def isDepot(u, v):
    return u == "1" or v == "1"

def getEdgesInOptimalRoute(routes):
    edges_in_optimal_route = set()

    for route in routes:
        curr = routes[route]

        for index in range(0, len(curr) - 1):
            coordStr1, coordStr2 = createEdgeStrings(curr[index], curr[index + 1])

            if not checkEdgeExists(edges_in_optimal_route, coordStr1, coordStr2):
                edges_in_optimal_route.add(coordStr1)
    return edges_in_optimal_route

def initIncidentMatrix(coords, matrix_size):
    arr = np.zeros((matrix_size, matrix_size))
    return labelMatrix(coords, arr)

def labelMatrix(coords, arr):
    row_labels = [row for row in coords]
    column_labels = [col for col in coords]
    incidence_matrix = pd.DataFrame(arr, columns=column_labels, index=row_labels)

    return incidence_matrix 

def createEdgesDF(coords, routes):
    edges_in_optimal_route = getEdgesInOptimalRoute(routes)
    incidenceMatrix = initIncidentMatrix(coords, len(coords))
    edgesDict = defaultdict(list)
    edges_set = set()
    dict_global_edge_rank = {}
    index, row, column = 0, 1, 1
    
    for u, coord_u in coords.items():
        for v, coord_v in coords.items():
            coordStr1, coordStr2 = stringEdgeBuilder(u, v), stringEdgeBuilder(v, u)

            edge_weight = calculateWeight(coord_u, coord_v)

            if not compareCoordID(u, v) and not checkEdgeExists(edges_set, coordStr1, coordStr2):
                edges_set.add(coordStr1)

                edgesDict[c.U_X].append(coord_u[0])
                edgesDict[c.U_Y].append(coord_u[1])
                edgesDict[c.U_NODE_ID].append(u)

                edgesDict[c.V_X].append(coord_v[0])
                edgesDict[c.V_Y].append(coord_v[1])
                edgesDict[c.V_NODE_ID].append(v)


                edgesDict[c.EDGE_WEIGHT].append(edge_weight)
                dict_global_edge_rank[index] = edge_weight
                index += 1

                if checkEdgeExists(edges_in_optimal_route, coordStr1, coordStr2):
                    edgesDict[c.IS_OPTIMAL_EDGE].append(1)
                else:
                    edgesDict[c.IS_OPTIMAL_EDGE].append(0)
                    
                if isDepot(u, v):
                    edgesDict[c.IS_DEPOT].append(1)
                else:
                    edgesDict[c.IS_DEPOT].append(0)


            incidenceMatrix[str(row)][str(column)] = edge_weight
            column += 1
        column = 0
        row += 1

    return pd.DataFrame(edgesDict), dict_global_edge_rank, incidenceMatrix

def buildGraph(df, isOptimalEdgesOnly):
    plt.rcParams["figure.figsize"] = [16,9]
    
    if isOptimalEdgesOnly:
        graph = df[[c.U_NODE_ID, c.V_NODE_ID]].where(df[c.IS_OPTIMAL_EDGE] == 1)
    else:
        graph = df[[c.U_NODE_ID, c.V_NODE_ID]]

    G = nx.from_pandas_edgelist(graph, c.U_NODE_ID, c.V_NODE_ID)

    return G

def plotGraph(G):
    nx.draw(G, with_labels=True)
    plt.show()
# In[ ]:




