#!/usr/bin/env python
# coding: utf-8

# In[2]:

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
    routes = x[2:]
    routes.insert(0, "1")

    return routes

def read_instance(file):
    COORD_FLAG, DEMAND_FLAG = False, False

    xc, yc = [], []
    coords, q, coords_node_id_dict = {}, {}, {}

    fh = open("../Instances/Instances/" + file, 'r')
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


def read_solution(file):
    fh = open("../Instances/Solutions/" + file, 'r')  # A-n32-k5-solution.txt
    routes = {}
    for i, line in enumerate(fh):
        if "Route #" in line:
            routes[i] = parse_routes(line)
            routes[i] = [x for x in routes[i] ]
            routes[i].append("1")
    return routes


# In[ ]:





# In[ ]:




