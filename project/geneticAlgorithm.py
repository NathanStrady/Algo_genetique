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

    def fitnesses(self, pop):
        fitness = []
        for i in range(len(pop)):
            fitness.append(self.calculate_fitness(pop[i]))
        return fitness

    def tournament_selection(self, population, fitnesses, k, num_selections):
        selected = []
        for _ in range(num_selections):
            tournament = rd.sample(range(len(population)), k)
            winner = max(tournament, key=lambda i: fitnesses[i])
            selected.append(population[winner])
        return selected

    def crossover(self):
        return

    def mutation(self):
        return

    def ga_tournament(self, taille_pop):
        init = self.initialisation(taille_pop)
        fitnesses = self.fitnesses(init)
        selection = self.tournament_selection(init, fitnesses, 2, len(init)//2)
        return init
