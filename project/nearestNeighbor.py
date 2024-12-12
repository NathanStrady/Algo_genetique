class NearestNeighbor:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph.matrix)

    def linear_search(self, start):
        if start not in self.graph.vertices:
            raise ValueError(f"Sommet {start} pas dans le graphe.")

        start_index = self.graph.vertices.index(start)
        path = [start]
        visited = [False] * self.n
        visited[start_index] = True
        current_node = start_index
        distance = 0

        for i in range(self.n - 1):
            nearest_node = None
            min_distance = float('inf')
            for j in range(len(self.graph.matrix[i])):
                if not visited[j] and self.graph.matrix[current_node][j] < min_distance:
                    nearest_node = j
                    min_distance = self.graph.matrix[current_node][j]

            path.append(self.graph.vertices[nearest_node])
            visited[nearest_node] = True
            distance += min_distance
            current_node = nearest_node

        distance += self.graph.matrix[current_node][start_index]
        path.append(start)
        return path, distance


