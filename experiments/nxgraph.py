"""Graph implementation of warehouse"""

import networkx as nx
import json


# import matplotlib.pyplot as plt

rows, cols = 16, 8  # subdivision of library top-down view into grid

G = nx.Graph()
G.add_node(range(rows * cols))  # create graph with (rows x cols) nodes

# Adding edges
edges = []
edges += [(i, i + 8) for i in range(0, 120, 8)]  # left vertical edges
edges += [(i, i + 8) for i in range(7, 127, 8)]  # right vertical edges
for j in [range(k, k + 7) for k in [0, 24, 32, 64, 88, 96, 120]]:
    for i in j:
        edges.append((i, i + 1))  # horizontal edges

G.add_edges_from(edges)


# Paths
all_paths = dict(nx.all_pairs_shortest_path(G))
x, y = 0, 31
optimal_route = all_paths[x][y]

# Test
for i in range(1, 129):
    if i - 1 in optimal_route:
        if i % 8 == 0:
            print("*", end="\n")
        else:
            print("*", end="\t")
    else:
        if i % 8 == 0:
            print(i - 1, end="\n")
        else:
            print(i - 1, end="\t")
print("optimal_route is {}".format(optimal_route))
print("Path length is {}".format(len(optimal_route)))

# JSON
path = {
    "path": optimal_route,
    "path_length:": len(optimal_route)
}

json_data = json.dumps(path)

# Visualizing
# nx.draw_networkx(G)
# plt.show()
