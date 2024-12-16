import networkx as nx


class Graph:
    INF = float("inf")

    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[self.INF] * len(vertices) for _ in range(len(vertices))]

    def __str__(self):
        graph_str = "  " + " ".join(str(v) for v in self.vertices) + "\n"
        for i in range(len(self.vertices)):
            graph_str += self.vertices[i] + " "
            graph_str += (
                    " ".join(
                        "." if self.matrix[i][j] == float("inf") else str(self.matrix[i][j])
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
