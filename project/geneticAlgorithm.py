import random as rd
import time

from PyQt6.uic.properties import QtCore

from project.nearestNeighbor import NearestNeighbor


class GeneticAlgorithm:
    def __init__(self, graph):
        self.graph = graph
        self.nearestNeighbor = NearestNeighbor()

    def initialisation_linear_search(self, taille_pop):
        pop = []
        for i in range(taille_pop):
            start_vertex = rd.choice(self.graph.vertices)
            pop.append(self.nearestNeighbor.linear_search(self.graph, start_vertex, rd.uniform(0.5, 0.9)))
        return pop

    def initialisation_random_search(self, taille_pop):
        pop = []
        for i in range(taille_pop):
            start_vertex = rd.choice(self.graph.vertices)
            pop.append(self.nearestNeighbor.random_search(self.graph, start_vertex))
        return pop

    def calculate_fitness(self, path):
        total = 0
        n = len(path)
        for i in range(n - 1):
            u, v = self.graph.vertices.index(path[i]), self.graph.vertices.index(path[i + 1])
            total += self.graph.matrix[u][v]
        u, v = self.graph.vertices.index(path[n - 1]), self.graph.vertices.index(path[0])
        total += self.graph.matrix[u][v]
        return 1 / total

    def fitnesses(self, pop):
        fitness = []
        for i in range(len(pop)):
            fitness.append(self.calculate_fitness(pop[i]))
        return fitness

    def best_path(self, population, fitnesses):
        best_index = fitnesses.index(max(fitnesses))
        return population[best_index], fitnesses[best_index]

    def tournament_selection(self, population, fitnesses, k, num_parents):
        selected_parents = []
        for _ in range(num_parents):
            tournament = rd.sample(range(len(population)), k)
            winner = max(tournament, key=lambda i: fitnesses[i])
            selected_parents.append(population[winner])
        return selected_parents

    def ranking_selection(self, population, fitnesses, num_selections):
        selected = []
        currentPop = population
        currentFit = fitnesses
        for _ in range(num_selections):
            bestNode = max(currentFit)
            index = currentFit.index(bestNode)
            selected.append(currentPop[index])
            currentPop.pop(index)
            currentFit.pop(index)
        return selected

    def cycle_crossover(self, p1, p2):
        c1 = ['-'] * len(p1)
        c2 = ['-'] * len(p2)

        n = len(p1)
        cycles = []
        visited = [False] * n

        for i in range(n):
            if not visited[i]:
                current_cycle = []
                j = i
                while not visited[j]:
                    visited[j] = True
                    current_cycle.append(p1[j])
                    j = p1.index(p2[j])
                cycles.append(current_cycle)

        for cycle in cycles:
            is_odd_cycle = (cycles.index(cycle) % 2 == 0)
            for value in cycle:
                i = p1.index(value)
                if is_odd_cycle:
                    c1[i] = p1[i]
                    c2[i] = p2[i]
                else:
                    c1[i] = p2[i]
                    c2[i] = p1[i]

        return c1, c2

    def mutation(self, path):
        n = len(path) - 1
        i, j = round(rd.uniform(0, n)), round(rd.uniform(0, n))
        path[i], path[j] = path[j], path[i]
        return path

    def ga_tournament_linear_search(self, nb_pop, nb_generation, update_display_callback):
        start_time = time.time()
        best = None
        population = self.initialisation_linear_search(nb_pop)
        fitnesses = self.fitnesses(population)
        best_fitnesses = []
        for gen in range(nb_generation):
            new_population = []
            selected = self.tournament_selection(population, fitnesses, k=4, num_parents=nb_pop // 2)
            while len(new_population) < nb_pop:
                p1 = rd.choice(selected)
                p2 = rd.choice(selected)
                c1, c2 = self.cycle_crossover(p1, p2)
                c1 = self.mutation(c1)
                c2 = self.mutation(c2)
                new_population.extend([c1, c2])
            population = new_population
            fitnesses = self.fitnesses(population)
            best = self.best_path(population, fitnesses)
            best_fitnesses.append(best[1])
            print(f"Generation {gen + 1}: Best path fitness = {best[1]} Path: {best[0]}")
        end_time = time.time()
        execution_time = end_time - start_time
        update_display_callback(self.graph.to_nx_graph(), nb_generation, best[0], best_fitnesses, execution_time)
        return best

    def ga_tournament_random_search(self, nb_pop, nb_generation, update_display_callback):
        start_time = time.time()
        best = None
        population = self.initialisation_random_search(nb_pop)
        fitnesses = self.fitnesses(population)
        best_fitnesses = []
        for gen in range(nb_generation):
            new_population = []
            selected = self.tournament_selection(population, fitnesses, k=4, num_parents=nb_pop // 2)
            while len(new_population) < nb_pop:
                p1 = rd.choice(selected)
                p2 = rd.choice(selected)
                c1, c2 = self.cycle_crossover(p1, p2)
                c1 = self.mutation(c1)
                c2 = self.mutation(c2)
                new_population.extend([c1, c2])
            population = new_population
            fitnesses = self.fitnesses(population)
            best = self.best_path(population, fitnesses)
            best_fitnesses.append(best[1])
            print(f"Generation {gen + 1}: Best path fitness = {best[1]} Path: {best[0]}")
        end_time = time.time()
        execution_time = end_time - start_time
        update_display_callback(self.graph.to_nx_graph(), nb_generation, best[0], best_fitnesses, execution_time)
        return best



    def ga_ranking_random_search(self, nb_pop, nb_generation, update_display_callback):
        start_time = time.time()
        best = None
        population = self.initialisation_random_search(nb_pop)
        fitnesses = self.fitnesses(population)
        best_fitnesses = []
        for gen in range(nb_generation):
            new_population = []
            selected = self.ranking_selection(population, fitnesses, nb_pop // 2)
            while len(new_population) < nb_pop:
                p1 = rd.choice(selected)
                p2 = rd.choice(selected)
                c1, c2 = self.cycle_crossover(p1, p2)
                c1 = self.mutation(c1)
                c2 = self.mutation(c2)
                new_population.extend([c1, c2])
            population = new_population
            fitnesses = self.fitnesses(population)
            best = self.best_path(population, fitnesses)
            best_fitnesses.append(best[1])
            print(f"Generation {gen + 1}: Best path fitness = {best[1]} Path: {best[0]}")
        end_time = time.time()
        execution_time = end_time - start_time
        update_display_callback(self.graph.to_nx_graph(), nb_generation, best[0], best_fitnesses, execution_time)
        return best

    def ga_ranking_linear_search(self, nb_pop, nb_generation, update_display_callback):
        start_time = time.time()
        best = None
        population = self.initialisation_linear_search(nb_pop)
        fitnesses = self.fitnesses(population)
        best_fitnesses = []
        for gen in range(nb_generation):
            new_population = []
            selected = self.ranking_selection(population, fitnesses, nb_pop // 2)
            while len(new_population) < nb_pop:
                p1 = rd.choice(selected)
                p2 = rd.choice(selected)
                c1, c2 = self.cycle_crossover(p1, p2)
                c1 = self.mutation(c1)
                c2 = self.mutation(c2)
                new_population.extend([c1, c2])
            population = new_population
            fitnesses = self.fitnesses(population)
            best = self.best_path(population, fitnesses)
            best_fitnesses.append(best[1])
            print(f"Generation {gen + 1}: Best path fitness = {best[1]} Path: {best[0]}")
        end_time = time.time()
        execution_time = end_time - start_time
        update_display_callback(self.graph.to_nx_graph(), nb_generation, best[0], best_fitnesses, execution_time)
        return best