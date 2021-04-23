import FileParser as fp
import PathFinder as pf
import SetSolver as set_solver
import re
import os
import sys
from linecache import getline
from gurobipy import Model, GRB, quicksum
from pathlib import Path

# Entrypoint for the set based formulation solver

def solve(is_pruned):
    path = os.getcwd() + "/Instances/Instances - Prune/"
    instances = fp.get_instances(path)

    for instance in instances:
        print("INSTANCE: ", instance)
        temp = path
        temp += instance
        set_solver.solve(temp, instance, is_pruned)
        print()