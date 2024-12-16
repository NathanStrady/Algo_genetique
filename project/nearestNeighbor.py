import random as rd
class NearestNeighbor:

    def linear_search(self, graph, start, p=0.5):
        if start not in graph.vertices:
            raise ValueError(f"Sommet {start} pas dans le graphe.")

        n = len(graph.vertices)
        start_index = graph.vertices.index(start)
        path = [start]
        visited = [False] * n
        visited[start_index] = True
        current_node = start_index

        for i in range(n - 1):
            nearest_node = None
            candidates = [j for j in range(len(graph.matrix[current_node])) if not visited[j]]
            if candidates:
                if rd.random() < p:
                    nearest_node = rd.choice(candidates)
                else:
                    nearest_node = min(candidates, key=lambda x: graph.matrix[current_node][x])
            path.append(graph.vertices[nearest_node])
            visited[nearest_node] = True
            current_node = nearest_node

        path.append(start)
        return path
