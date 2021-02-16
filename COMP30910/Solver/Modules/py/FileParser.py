#!/usr/bin/env python
# coding: utf-8

# In[2]:


def parseCoords(line):
    x = line.split()
    return [x[0], x[1], x[2]]

def parseDemand(line):
    x = line.split()
    return [int(x[0]), int(x[1])]

def parseRoutes(line):
    x = line.split()
    parsedRoutes = x[2:]
    parsedRoutes.insert(0, "1")

    return parsedRoutes

def readInstance(file):
    COORD_FLAG, DEMAND_FLAG = False, False

    xc, yc = [], []
    coords, q = {}, {}

    fh = open(file, 'r')
    for i, line in enumerate(fh):
        if "NODE_COORD_SECTION" in line:
            COORD_FLAG = True
        elif "DEMAND_SECTION" in line:
            COORD_FLAG = False
            DEMAND_FLAG = True
        elif "DEPOT_SECTION" in line:
            DEMAND_FLAG = False
        elif COORD_FLAG:
            coord = parseCoords(line)
            xc.append(coord[1])
            yc.append(coord[2])
            coords[coord[0]] = [coord[1], coord[2]]
        elif DEMAND_FLAG:
            demand = parseDemand(line)
            q[demand[0]] = demand[1]
    fh.close()

    return xc, yc, coords, q


def readSolution(file):
    fh = open(file, 'r')  # A-n32-k5-solution.txt
    routes = {}
    for i, line in enumerate(fh):
        if "Route #" in line:
            routes[i] = parseRoutes(line)
            routes[i] = [x for x in routes[i] ]
            routes[i].append("1")
    return routes


# In[ ]:





# In[ ]:




