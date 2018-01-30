"""Implementation of an undirected graph using an adjacency matrix.

Graph consists of a Node class which can hold data as well as a Graph class which adds the ability to work with edges between nodes. Finally, Floyd-Warshall's all-pairs shortest path algorithm is implemented on top of the underlying adjacency matrix data structure to obtain a useful list of shortest path.

The adjacency matrix implementation is well suited for a warehouse-type environment.

Current implementation is based on numpy and assumes that vertices are integer only. Future implementations could made data held by the nodes generic, include optimizing compile times, or using an external library instead of implementing a graph from scratch.

Based on http://bit.ly/java-adjmatrixgraph.
"""
import numpy as np
from random import randrange


class AdjacencyMatrixGraph(object):
    """Represents a node in an undirected graph"""

    def __init__(self, V, E=0):
        """Adjacency matrix of size V x V with random edges if E is provided"""
        try:
            if V < 0:
                raise ValueError("V less than 0")
            if E < 0:
                raise ValueError("E less than 0")
            if E > V * (V - 1) + V:
                raise ValueError("Too many edges")
        except ValueError as err:
            print(err)

        self.V = V
        self.E = E
        self.adjacency_matrix = np.full((V, V), np.False_)

        # can be inefficient
        for _ in range(E):
            v_1 = randrange(0, V)
            v_2 = randrange(0, V)
            # add_edge(v_1, v_2)

    def num_vertices(self):
        """Getter for number of vertices"""
        return self.V

    def num_edges(self):
        """Getter for number of edges"""
        return self.E

    def add_edge(self, v_1, v_2):
        """Add undirected edge v_1-v_2"""
        if self.adjacency_matrix[v_1][v_2] != np.False_:
            self.E += 1
        self.adjacency_matrix[v_1][v_2] = np.True_
        self.adjacency_matrix[v_2][v_1] = np.True_

    def contains(self, v_1, v_2):
        """Does the graph contain edge v_1-v_2"""
        return self.adjacency_matrix[v_1][v_2] == np.True_
