import networkx as nx
from matplotlib import pyplot as plt

from project.graph import Graph
from project.geneticAlgorithm import GeneticAlgorithm


def plot_graph(graph):
    nx_graph = graph.to_nx_graph()
    pos = nx.spring_layout(nx_graph, k=10, iterations=50)

    plt.figure(figsize=(15, 10))
    plt.title("Graph Visualization")
    nx.draw(
        nx_graph,
        pos,
        with_labels=True,
        node_size=800,
        node_color="lightblue",
        font_size=10,
    )

    labels = nx.get_edge_attributes(nx_graph, "weight")
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=labels)
    plt.show()

def main():
    graph = Graph.generate_random_graph(10, 5)
    plot_graph(graph)
    GA = GeneticAlgorithm(graph)
    print(GA.ga_tournament(50))


if __name__ == "__main__":
    main()
