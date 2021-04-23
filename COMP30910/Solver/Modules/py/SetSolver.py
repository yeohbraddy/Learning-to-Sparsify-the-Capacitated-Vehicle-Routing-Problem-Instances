import localsolver
import sys
import os
import pandas as pd
import math
import FileParser as fp

# Implementation of the set based formulation solver

def solve(instance_file, file_name, is_pruned):
 
    # Reads instance data
    xc, yc, coords, q, Q, p, n, coords_node_id_dict = fp.read_instance(instance_file)
    
    num_of_customers, distance_matrix, distance_warehouses, demands = calc_variables(n, xc, yc, q, is_pruned)

    capacity = Q
    num_of_trucks = p

    with localsolver.LocalSolver() as ls:
        mdl = ls.model

        # Sequence of customers visited by each truck.
        customers_sequences = [mdl.list(num_of_customers)
                               for k in range(num_of_trucks)]

        # All customers must be visited by the trucks
        mdl.constraint(mdl.partition(customers_sequences))

        demands_arr = mdl.array(demands)

        distance_arr = mdl.array()
        for n in range(num_of_customers):
            distance_arr.add_operand(mdl.array(distance_matrix[n]))

        distance_warehouse_array = mdl.array(distance_warehouses)

        route_distances = [None] * num_of_trucks

        # A truck is used if it visits at least one customer
        trucks_used = [(mdl.count(customers_sequences[k]) > 0)
                       for k in range(num_of_trucks)]
        num_of_trucks_used = mdl.sum(trucks_used)

        for k in range(num_of_trucks):
            seq = customers_sequences[k]
            count = mdl.count(seq)

            # Quantity in each truck
            demand_selector = mdl.lambda_function(
                lambda i: demands_arr[seq[i]])
            route_quantity = mdl.sum(mdl.range(0, count), demand_selector)
            mdl.constraint(route_quantity <= capacity)

            # Distance traveled by each truck
            distance_selector = mdl.lambda_function(
                lambda i: mdl.at(distance_arr, seq[i-1], seq[i]))
            route_distances[k] = mdl.sum(mdl.range(1, count), distance_selector) + \
                mdl.iif(
                    count > 0, distance_warehouse_array[seq[0]] + distance_warehouse_array[seq[count-1]], 0)

        # Total distance traveled
        total_distance = mdl.sum(route_distances)

        # Objective: minimize the number of trucks used
        mdl.minimize(num_of_trucks_used)

        # Objective: minimize the distance traveled
        mdl.minimize(total_distance)

        mdl.close()
        
        ls.solve()

        # Writes the solution in a file with the following format:
        # For each truck the nodes visited
        #
        sol_file = os.getcwd() + "/Instances/Solutions - Prune/" + file_name[:len(file_name) - 4] + "-solution.txt"
        with open(sol_file, 'w') as f:
            for k in range(num_of_trucks):
                if trucks_used[k].value != 1:
                    continue
                f.write("Route #" + str(k + 1) + ": ")
                for customer in customers_sequences[k].value:
                    f.write("%d " % (customer + 2))
                f.write("\n")

def calc_variables(num_of_customers, xc, yc, demands, is_pruned):
    
    num_of_nodes = num_of_customers + 1
    
    customers_x = xc[1:]
    customers_y = yc[1:]
    depot_x = xc[0]
    depot_y = yc[0]

    # Compute distance matrix
    distance_matrix = calc_distance_matrix(customers_x, customers_y, is_pruned)
    distance_warehouses = calc_distance_warehouse(
        depot_x, depot_y, customers_x, customers_y)

    demands_list = list(demands.values())[1:]
    
    return num_of_customers, distance_matrix, distance_warehouses, demands_list

# Computes the distance matrix
def calc_distance_matrix(customers_x, customers_y, is_pruned):
    path = os.getcwd() + "/Data/"
    df = pd.read_csv(path + 'data_pruned.csv',
                     index_col=0) if is_pruned else pd.DataFrame()
    
    num_of_customers = len(customers_x)
    distance_matrix = [[None for i in range(
        num_of_customers)] for j in range(num_of_customers)]
    for i in range(num_of_customers):
        distance_matrix[i][i] = 0
        for j in range(num_of_customers):
            dist = calc_dist(
                customers_x[i], customers_x[j], customers_y[i], customers_y[j])

            is_optimal_edge = False
            
            # Keeping only the positively predicted edges
            if is_pruned:
                row = df.loc[
                    (df['U_X'] == customers_x[i]) &
                    (df['U_Y'] == customers_y[i]) &
                    (df['V_X'] == customers_x[j]) &
                    (df['V_Y'] == customers_y[j]) &
                    (df['IS_OPTIMAL_EDGE_PRUNE'] == 1)
                ]
                
                if len(row) > 0:
                    is_optimal_edge = True

                distance_matrix[i][j] = dist if is_optimal_edge else 100 * 100
                distance_matrix[j][i] = dist if is_optimal_edge else 100 * 100
            else:
                distance_matrix[i][j] = dist
                distance_matrix[j][i] = dist
    return distance_matrix

# Computes the distances to warehouse
def calc_distance_warehouse(depot_x, depot_y, customers_x, customers_y):
    num_of_customers = len(customers_x)
    distance_warehouses = [None] * num_of_customers
    for i in range(num_of_customers):
        dist = calc_dist(depot_x, customers_x[i], depot_y, customers_y[i])
        distance_warehouses[i] = dist
    return distance_warehouses

def calc_dist(xi, xj, yi, yj):
    exact_dist = math.sqrt(math.pow(xi - xj, 2) + math.pow(yi - yj, 2))
    return int(math.floor(exact_dist + 0.5))
