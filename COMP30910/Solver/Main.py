from pathlib import Path
from gurobipy import Model, GRB, quicksum
from linecache import getline
import os
import re
import sys
sys.path.append(str(Path(os.getcwd())) + '\COMP30910\Solver\Modules\py')


import TwoIndexFormulation as tif, FeatureEngineering as fe, Model as m

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
step_three = True
step_four = False

if step_one:
    print_str("SOLVING..")
    tif.solve(False)
    print_completed()
    
if step_two:
    print_str("GENERATING MODEL FEATURES FOR INSTANCE..")
    fe.generate_features(True)
    print_completed()

if step_three:  
    print_str("PRUNING")
    m.prune_instance()
    print_completed()
      
if step_four:
    print_str("SOLVING PRUNED INSTANCE..")
    tif.solve(True)
    print_completed()
