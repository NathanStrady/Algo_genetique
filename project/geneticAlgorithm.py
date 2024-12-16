import random as rd


class GeneticAlgorithm:
    def __init__(self, graph, nearestNeighbor):
        self.graph = graph
        self.nearestNeighbor = nearestNeighbor

    def generation(self, taille_pop):
        pop = []
        for i in range(taille_pop):
            start_vertex = rd.choice(self.graph.vertices)
            pop.append(self.nearestNeighbor.linear_search(start_vertex))
        return pop
