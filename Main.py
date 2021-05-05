from pathlib import Path
from gurobipy import Model, GRB, quicksum
from linecache import getline
import os
import re
import sys
sys.path.append(str(Path(os.getcwd())) + '/Modules/py')
import SetBasedFormulation as sbf
import FeatureEngineering as fe

def print_str(str):
    print("\n" + '=' * 150)
    print(str)
    print('=' * 150)

def print_completed():
    print_str("COMPLETED")

generate_training_data = False
generate_test_data = True
solve_pruned = False
solve_unpruned = False

if generate_training_data:
    print_str("GENERATING TRAINING DATA..")
    fe.generate_features(is_prune=False)
    print_completed()
    
if generate_test_data:
    print_str("GENERATING MODEL FEATURES FOR INSTANCE TO PRUNE..")
    fe.generate_features(is_prune=True)
    print_completed()

if run_solver:
    print_str("SOLVING..")
    sbf.solve(False)
    print_completed()

    print_str("SOLVING PRUNED INSTANCE..")
    sbf.solve(True)
    print_completed()
