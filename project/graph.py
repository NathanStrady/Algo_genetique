import networkx as nx
import random as rd

class Graph:
    INF = float("inf")

    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[self.INF] * len(vertices) for _ in range(len(vertices))]

    def __str__(self):
        graph_str = "  " + "   ".join(str(v) for v in self.vertices) + "\n"
        for i in range(len(self.vertices)):
            graph_str += self.vertices[i] + " "
            graph_str += (
                    " ".join(
                        f"{self.matrix[i][j]:>3}" if self.matrix[i][j] != float("inf") else "inf"
                        for j in range(len(self.vertices))
                    )
                    + "\n"
            )
        return graph_str

    def add_edge(self, i, j, weight):
        u_index = self.vertices.index(i)
        v_index = self.vertices.index(j)
        self.matrix[u_index][v_index] = weight
        self.matrix[v_index][u_index] = weight

    def to_nx_graph(self):
        G = nx.Graph()
        for i, vertex in enumerate(self.vertices):
            G.add_node(vertex)
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.matrix[i][j] != self.INF:
                    G.add_edge(
                        self.vertices[i], self.vertices[j], weight=self.matrix[i][j]
                    )
        return G

    def max_edge(self):
        num_vertices = len(self.vertices)
        return (num_vertices * (num_vertices - 1 )) // 2

    @staticmethod
    def generate_random_graph(num_vertices, max_weight=10):
        vertices = [str(i) for i in range(num_vertices)]
        graph = Graph(vertices)
        max_nb_edges = graph.max_edge()
        edges_added = 0

        while edges_added < max_nb_edges:
            u = rd.choice(vertices)
            v = rd.choice(vertices)
            if u != v and graph.matrix[graph.vertices.index(u)][graph.vertices.index(v)] == Graph.INF:
                weight = rd.randint(1, max_weight)
                graph.add_edge(u, v, weight)
                edges_added += 1
        return graph




