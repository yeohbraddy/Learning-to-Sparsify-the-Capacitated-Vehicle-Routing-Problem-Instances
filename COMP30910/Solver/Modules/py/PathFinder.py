import os


def create_solution_file(arcs, cost, file_name):
    print("Building routes..")
    routes = build_routes(arcs)

    print("Converting to string..")
    text = to_string(routes, cost)

    print("Writing string to file..")
    write_to_file(text, file_name)


def build_routes(arcs):
    num_of_edges_from_origin = 0
    for a in arcs:
        if a[0] == 0:
            num_of_edges_from_origin += 1

    arcs.sort(key=lambda tup: (tup[0], tup[1]))
    routes = {}
    for edge in range(0, num_of_edges_from_origin):
        node_u = arcs[edge][1]
        route = [str(node_u)]
        li = find_route(node_u, arcs[num_of_edges_from_origin:], route)
        li.pop()
        routes[edge] = li

    return routes


def to_string(routes, cost):
    text = ""
    for k in routes:
        text += "Route #" + str(k + 1) + ": "
        for node in routes[k]:
            text += node + " "
        text += "\n"
    text += "Cost " + cost

    return text


def write_to_file(text, file_name):
    path = os.getcwd() + "\COMP30910\Solver\Instances\Solutions - Engineered/"
    f = open(path + file_name, "w")
    f.write(text)
    f.close()


def find_route(node_u, arcs, route):
    while node_u != 0:
        start = 0
        end = len(arcs) - 1

        while start <= end:
            middle = start + (end - start) // 2
            mid = arcs[middle][0]
            if mid < node_u:
                start = middle + 1
            elif mid > node_u:
                end = middle - 1
            else:
                node_u = arcs[middle][1]
                route = route + [str(node_u)]
                break
    return route
