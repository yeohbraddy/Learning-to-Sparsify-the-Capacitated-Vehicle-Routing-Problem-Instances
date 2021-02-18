import matplotlib.pyplot as plt
import FileParser as fp
import numpy as np
import matplotlib.pyplot as plt
from gurobipy import Model, GRB, quicksum

def solve(file_name):
    xc, yc, coords, q, Q, p, n = fp.read_instance(file_name)
    
    plot_instances(xc, yc)

    # Number of clients
    N = [i for i in range(1, n+1)] 

    # Number of nodes (including depot)
    V = [0] + N 

    # Arcs
    A = [(i, j) for i in V for j in V] 

    # Cost
    c = {(i, j): np.hypot(xc[i] - xc[j], yc[i] - yc[j]) for i, j in A}

    mdl = Model('CVRP')

    x = mdl.addVars(A, vtype=GRB.CONTINUOUS)
    u = mdl.addVars(N, vtype=GRB.CONTINUOUS)
    mdl.update()

    mdl.modelSense = GRB.MINIMIZE
    mdl.setObjective(quicksum(c[i, j] * x[i, j] for i, j in A))
    mdl.update()

    mdl.addConstrs(quicksum(x[i, j] for i in V if i != j) == 1 for j in N)
    mdl.update()

    mdl.addConstrs(quicksum(x[i, j] for j in V if j != i) == 1 for i in N)
    mdl.update()

    mdl.addConstr(quicksum(x[i, 0] for i in V) == p)
    mdl.update()

    mdl.addConstr(quicksum(x[0, j] for j in V) == p)
    mdl.update()

    mdl.addConstrs((u[j] - u[i]) >= (q[j] - Q*(1 - x[i, j])) for i in N for j in N if i != j)
    mdl.update()

    mdl.addConstrs(u[i] >= q[i] for i in N)
    mdl.addConstrs(u[i] <= Q for i in N)
    mdl.update()
    
    mdl.optimize()

    active_arcs = []
    non_active_arcs = []

    for a in A:
        if x[a].x > 0.99:
            active_arcs.append(a)
        else:
            non_active_arcs.append(a)

    plot_solution(active_arcs, xc, yc)

def plot_instances(xc, yc):
    plt.rcParams["figure.figsize"] = [16,9]
    plt.plot(xc[0], yc[0], c='r', marker='s')
    plt.scatter(xc[1:], yc[1:], c='black')


def plot_solution(arcs, xc, yc):
    plt.rcParams["figure.figsize"] = [16,9]

    for i, j in arcs:
        plt.plot([xc[i], xc[j]], [yc[i], yc[j]], c='black', zorder=0)
    plt.plot(xc[0], yc[0], c='r', marker='s')
    plt.scatter(xc[1:], yc[1:], c='black')