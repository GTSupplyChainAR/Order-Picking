"""Implementation of a graph data structure using python's defaultdict and sets
which is stored as an adjacency list.

Using collections.defaultdict instead of dict avoids a KeyError from trying to
add keys that might not exist. defaultdict creates a new key with a default value.

The most optimal paths throughout the warehouse are precomputed using Floyd Warshall's
All-Pairs Shortest Path Algorithm. The adjacency matrix generated from running
this algorithm is used to computed any particular shortest path between two nodes in
the graph.

Inspired by http://bit.ly/graph-python.
"""

from collections import defaultdict
import numpy as np


class Graph(object):
    """Graph class, undirected by default."""

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """Add connections (list of tuple pairs) to graph"""
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """Add connection between node1 and node2"""
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """Remove all references to node"""
        for _, connections in self._graph.items():
            try:
                connections.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """Check if edge exists between node1 and node2"""
        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=None):
        """TODO Find any path between node1 and node2 (may not be shortest YET)"""
        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def adjacency_matrix(self):
        """TODO Convert internal representation to an adjacency matrix"""
        num = len(self._graph)
        matrix = [["inf" for i in range(num)]
                  for j in range(num)]  # create num x num matrix filled with "inf"
        for i, j in [(k, k) for k in range(5)]:  # simplify later
            matrix[i][j] = 0
        for k, v in self._graph.items():
            k
        return matrix

    def __str__(self):
        """Returns a string representation of the graph."""
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


connections = [(1, 2), (2, 3), (2, 4),
               (3, 4), (5, 6), (6, 3)]
g = Graph(connections)
print(g.__str__())
print(g.adjacency_matrix())
