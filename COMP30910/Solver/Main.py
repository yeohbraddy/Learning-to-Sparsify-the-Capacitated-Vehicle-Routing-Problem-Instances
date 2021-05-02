from pathlib import Path
from gurobipy import Model, GRB, quicksum
from linecache import getline
import os
import re
import sys
sys.path.append(str(Path(os.getcwd())) + '/Modules/py')
import SetBasedFormulation as sbf
import FeatureEngineering as fe
# import Model as m

# 1. Run solver on instance to be pruned (Instances - Prune)
# 2. Feature Engineering on the Solution - Prune to get the data_prune.csv
# 3. Run ML model to get data_pruned.csv
# 4. Run solver again


def print_str(str):
    print("\n" + '=' * 150)
    print(str)
    print('=' * 150)


def print_completed():
    print_str("COMPLETED")


step_one = False
step_two = False
step_three = False
step_four = True

if step_one:
    print_str("SOLVING..")
    sbf.solve(False)
    print_completed()

if step_two:
#     print_str("GENERATING TRAINING DATA..")
#     fe.generate_features(is_prune=False)
#     print_completed()

    print_str("GENERATING MODEL FEATURES FOR INSTANCE TO PRUNE..")
    fe.generate_features(is_prune=True)
    print_completed()

if step_three:
    print_str("PRUNING")
#     m.prune_instance()
    print_completed()

if step_four:
    print_str("SOLVING PRUNED INSTANCE..")
    sbf.solve(True)
    print_completed()
