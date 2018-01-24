"""Graph implementation of warehouse"""

import networkx as nx
import matplotlib.pyplot as plt

rows, cols = 16, 8  # subdivision of library top-down view into grid

G = nx.Graph()
G.add_node(range(rows * cols))  # create graph with (rows x cols) nodes

# Adding edges
G.add_edges_from([(i, i + 8) for i in range(0, 120, 8)])  # left vertical edges
G.add_edges_from([(i, i + 8)
                  for i in range(7, 127, 8)])  # right vertical edges
for j in [range(k, k + 7) for k in [0, 24, 32, 64, 88, 96, 120]]:
    for i in j:
        G.add_edge(i, i + 1)  # horizontal edges

# Paths
path = dict(nx.all_pairs_shortest_path(G))

# Test
print(path[1][39])

# Visualizing
# nx.draw_networkx(G)
# plt.show()
