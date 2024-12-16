import random as rd
from project.nearestNeighbor import NearestNeighbor


class GeneticAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.nearestNeighbor = NearestNeighbor(graph)

    def initialisation(self, taille_pop):
        pop = []
        for i in range(taille_pop):
            start_vertex = rd.choice(self.graph.vertices)
            pop.append(self.nearestNeighbor.linear_search(start_vertex))
        return pop

    def calculate_fitness(self, path):
        total = 0
        for i in range(len(path) - 1):
            u, v = self.graph.vertices.index(path[i]), self.graph.vertices.index(path[i+1])
            total += self.graph.matrix[u][v]
        return 1/total
    def crossover(self):
        return

    def mutation(self):
        return

    def tournament_selection(self):
        return


    def ga_tournament(self, taille_pop):
        init = self.initialisation(taille_pop)
        print(self.calculate_fitness(init[0][0]))
        return init
