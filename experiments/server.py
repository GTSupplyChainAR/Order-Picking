"""Initializes server and exposes API endpoints
"""
from flask import Flask
import networkx as nx

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/graph")
def routing():
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
    paths = dict(nx.all_pairs_shortest_path(G))
    x, y = 0, 25
    route = paths[x][y]

    # Test
    string = ""
    for i in range(1, 129):
        if i - 1 in route:
            if i % 8 == 0:
                string += "*\n"
            else:
                string += "*\t"
        else:
            if i % 8 == 0:
                string += "{}\n".format(i - 1)
            else:
                string += "{}\t".format(i - 1)
    string += ("Route is {}".format(route))
    string += ("Path length is {}".format(len(route)))
    return string


if __name__ == '__main__':
    app.run(debug=True)
