class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matrix = [[float("inf")] * len(vertices) for _ in range(len(vertices))]

    def add_edge(self, i, j, weight):
        if i >= len(self.vertices) and j >= len(self.vertices):
            raise IndexError("Node out of bound")
        self.matrix[i][j] = weight
        self.matrix[j][i] = weight

    def __str__(self):
        graph_str = "  " + " ".join(str(v) for v in self.vertices) + "\n"
        for i in range(len(self.vertices)):
            graph_str += (
                self.vertices[i]
                + " "
                + " ".join(str(self.matrix[i][j]) for j in range(len(self.vertices)))
                + "\n"
            )
        return graph_str
