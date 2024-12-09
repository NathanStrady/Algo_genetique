class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.nbVertices = len(vertices)
        self.matrix = [[float("inf")] * self.nbVertices for _ in range(self.nbVertices)]

    def add_edge(self, i, j, weight):
        if i >= len(self.vertices) and j >= len(self.vertices):
            raise ("Node out of bound")
        self.matrix[i][j] = weight
        self.matrix[j][i] = weight

    def __str__(self):
        graph_str = "  " + " ".join(str(v) for v in self.vertices) + "\n"
        for i in range(self.nbVertices):
            graph_str += (
                self.vertices[i]
                + " "
                + " ".join(str(self.matrix[i][j]) for j in range(self.nbVertices))
                + "\n"
            )
        return graph_str
