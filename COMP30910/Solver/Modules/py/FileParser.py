#!/usr/bin/env python
# coding: utf-8

# To parse the instance files

import re
from os import listdir
from os.path import isfile, join

def get_instances(path):
    return [f for f in listdir(path) if isfile(join(path, f))]

def parse_num_vehicles(line):
    x = re.findall(r"No of trucks: [0-9]", line)
    return int(x[0][-1])

def parse_for_num(line):
    x = re.findall(r"[0-9]+", line)
    return int(x[0])

def parse_coords(line):
    x = line.split()
    return [x[0], int(x[1]), int(x[2])]

def parse_demand(line):
    x = line.split()
    return [int(x[0]), int(x[1])]

def parse_routes(line):
    x = line.split()
    # Solution file indicates customer 2 as node ID 1, so we need to increase it as depot ID is 1
    routes = [str(int(node) + 1) for node in x[2:]]
    routes.insert(0, "1")

    return routes

def read_instance(file):
    COORD_FLAG, DEMAND_FLAG = False, False

    xc, yc = [], []
    coords, q, coords_node_id_dict = {}, {}, {}

    fh = open(file, 'r')
    for i, line in enumerate(fh):
        if "CAPACITY" in line:
            Q = parse_for_num(line)
        elif "COMMENT" in line:
            p = parse_num_vehicles(line)
        elif "DIMENSION" in line:
            n = int(parse_for_num(line)) - 1 # number of clients
        elif "NODE_COORD_SECTION" in line:
            COORD_FLAG = True
        elif "DEMAND_SECTION" in line:
            COORD_FLAG = False
            DEMAND_FLAG = True
        elif "DEPOT_SECTION" in line:
            DEMAND_FLAG = False
        elif COORD_FLAG:
            coord = parse_coords(line)
            xc.append(coord[1])
            yc.append(coord[2])
            coords[coord[0]] = [coord[1], coord[2]]
            coords_node_id_dict[(coord[1], coord[2])] = coord[0]
        elif DEMAND_FLAG:
            demand = parse_demand(line)
            q[demand[0]] = demand[1]
    fh.close()

    return xc, yc, coords, q, Q, p, n, coords_node_id_dict

# For any particular route in the solution file, the format is given by:
# Route #num: 2 5 8 9 10
# where #num indicates the route number and the series of numbers that follow it are the IDs of the customer nodes.
# We know an ID of 1 is the depot, so the true route is 1 -> 2 -> 5 -> 8 -> 9 -> 10
# We need to convert each route in the solution file to its true route representation so we can extract edges for
# feature engineering, e.g, e0 = (1, 2), e1 = (2, 5), etc.
# This difference in format is due to the convention defined in literature.
def read_solution(file):
    fh = open(file, 'r')
    routes = {}
    for i, line in enumerate(fh):
        if "Route #" in line:
            routes[i] = parse_routes(line)
            routes[i] = [x for x in routes[i] ]
            routes[i].append("1")
    return routes



