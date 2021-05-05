#!/usr/bin/env python
# coding: utf-8

# Entrypoint for the two index formulation solver

import FileParser as fp
import PathFinder as pf
import TwoIndexSolver as solver
import re
import os
import sys
from linecache import getline
from gurobipy import Model, GRB, quicksum
from pathlib import Path


def solve(is_pruned):
    path = os.getcwd() + "/Instances/Instances - Prune/"
    instances = fp.get_instances(path)

    for instance in instances:
        print("INSTANCE: ", instance)
        temp = path
        temp += instance
        lp_relaxation, reduced_cost, active_arcs, cost = solver.solve(
            temp, instance, is_pruned=is_pruned)
        print()
