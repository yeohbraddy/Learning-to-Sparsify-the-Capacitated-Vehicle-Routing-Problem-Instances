import matplotlib.pyplot as plt
import FileParser as fp
import Graph as g
import os
import numpy as np
import matplotlib.pyplot as plt
from gurobipy import Model, GRB, quicksum
import pandas as pd


def solve(file_name, is_binary=True, enable_logging=True, is_pruned=False):
    xc, yc, coords, q, Q, p, n, coords_node_id_dict = fp.read_instance(
        file_name)

    path = os.getcwd() + "\COMP30910\Solver\Data/"
    df = pd.read_csv(path + 'data_pruned.csv',
                     index_col=0) if is_pruned else pd.DataFrame()

    # Number of clients
    N = get_nodes(df) if is_pruned else [i for i in range(1, n+1)]

    # Number of nodes (including depot)
    V = [0] + N

    # Arcs
    A = populate_arcs(df) if is_pruned else [(i, j) for i in V for j in V]

    # Cost
    c = {(i, j): np.hypot(xc[i] - xc[j], yc[i] - yc[j]) for i, j in A}

    mdl = Model('CVRP')
    if enable_logging is False:
        mdl.setParam("OutputFlag", 0)

    vtype = GRB.BINARY if is_binary else GRB.CONTINUOUS
    x = mdl.addVars(A, vtype=vtype)

    u = mdl.addVars(N, vtype=GRB.CONTINUOUS)
    mdl.update()

    mdl.modelSense = GRB.MINIMIZE
    mdl.setObjective(quicksum(c[i, j] * x[i, j] for i, j in A))
    mdl.update()

    mdl.addConstrs(quicksum(x[i, j] for i in V if i !=
                            j and (i, j) in x) == 1 for j in N)
    mdl.update()

    mdl.addConstrs(quicksum(x[i, j] for j in V if j !=
                            i and (i, j) in x) == 1 for i in N)
    mdl.update()

    mdl.addConstr(quicksum(x[i, 0] for i in V if (i, 0) in x) == p)
    mdl.update()

    mdl.addConstr(quicksum(x[0, j] for j in V if (0, j) in x) == p)
    mdl.update()

    mdl.addConstrs((u[j] - u[i]) >= (q[j] - Q*(1 - x[i, j]))
                   for i in N for j in N if i != j and (i, j) in x)
    mdl.update()

    mdl.addConstrs(u[i] >= q[i] for i in N)
    mdl.addConstrs(u[i] <= Q for i in N)
    mdl.update()

    mdl.Params.MIPGap = 0
    mdl.Params.PoolSearchMode = 2
    mdl.Params.PoolGap = 0

    mdl.optimize()

    active_arcs = []
    non_active_arcs = []
    lp_relaxation = {}
    reduced_cost = {}

    for a in A:
        lp_relaxation[a] = x[a].x
        if is_binary is False:
            reduced_cost[a] = x[a].getAttr(GRB.Attr.RC)
        if x[a].x > 0.99:
            active_arcs.append(a)
        else:
            non_active_arcs.append(a)

    if is_binary:
        for sol in range(mdl.SolCount):
            index = 0
            active_arcs = []
            mdl.setParam(GRB.Param.SolutionNumber, sol)
            values = mdl.Xn

            for a in A:
                if values[index] > 0.99:
                    active_arcs.append(a)
                index += 1
            plot_solution(active_arcs, xc, yc)
    return lp_relaxation, reduced_cost, active_arcs, str(round(mdl.getObjective().getValue()))


def plot_instances(xc, yc):
    plt.rcParams["figure.figsize"] = [16, 9]
    plt.plot(xc[0], yc[0], c='r', marker='s')
    plt.scatter(xc[1:], yc[1:], c='black')


def plot_solution(arcs, xc, yc):
    plt.rcParams["figure.figsize"] = [16, 9]

    for i, j in arcs:
        plt.plot([xc[i], xc[j]], [yc[i], yc[j]], c='black', zorder=0)
    plt.plot(xc[0], yc[0], c='r', marker='s')
    plt.scatter(xc[1:], yc[1:], c='black')


def populate_arcs(df):
    A = []
    pruned_dict = set()
    for index, row in df.iterrows():
        i, j = str(row['U_NODE_ID']), str(row['V_NODE_ID'])
        coord_str1, coord_str2 = g.create_edge_strings(
            i, j), g.create_edge_strings(j, i)
        if not g.check_edge_exists(pruned_dict, coord_str1, coord_str1) and row['IS_OPTIMAL_EDGE_PRUNE'] == 1:
            A.append((int(i) - 1, int(j) - 1))
            pruned_dict.add(coord_str1)
        if not g.check_edge_exists(pruned_dict, coord_str2, coord_str2) and row['IS_OPTIMAL_EDGE_PRUNE'] == 1:
            A.append((int(j) - 1, int(i) - 1))
            pruned_dict.add(coord_str2)
    return A


def get_nodes(df):
    nodes = set()
    for index, row in df.iterrows():
        node = row['U_NODE_ID'] - 1
        if node != 0 and row['IS_OPTIMAL_EDGE_PRUNE'] == 1 and node not in nodes:
            nodes.add(node)

    return list(nodes)
