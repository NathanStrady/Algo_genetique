import networkx as nx
from project.graph import Graph
from project.geneticAlgorithm import GeneticAlgorithm

def main():
    graph = Graph.generate_random_graph(15, 100)
    GA = GeneticAlgorithm(graph)
    GA.ga_tournament_random_search(50, 50)


if __name__ == "__main__":
    main()
