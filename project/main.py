import networkx as nx
from matplotlib import pyplot as plt

from project.graph import Graph
from project.geneticAlgorithm import GeneticAlgorithm
from project.nearestNeighbor import NearestNeighbor


def main():
    vertices = ["A", "B", "C", "D"]
    weights = [
        [0, 1, 2, 5],
        [1, 0, 1, 2],
        [2, 1, 0, 3],
        [5, 2, 3, 0],
    ]
    graph = Graph(vertices)

    for i in range(len(vertices)):
        for j in range(len(vertices)):
            if weights[i][j] != 0:
                graph.add_edge(vertices[i], vertices[j], weights[i][j])

    nearestNeighbor = NearestNeighbor(graph)
    geneticAlgo = GeneticAlgorithm(graph, nearestNeighbor)
    print(geneticAlgo.generation(10))

if __name__ == "__main__":
    main()
