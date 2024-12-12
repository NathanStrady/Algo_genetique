import networkx as nx
from matplotlib import pyplot as plt
from project.graph import Graph
from project.nearestNeighbor import NearestNeighbor


def main():
    vertices = ['A', 'B', 'C', 'D', 'E']
    graph = Graph(vertices)


    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 2)
    graph.add_edge('C', 'E', 3)
    graph.add_edge('D', 'E', 3)
    graph.add_edge('A', 'D', 5)

    nx_graph = graph.to_nx_graph()
    plt.figure(figsize=(8, 6))
    pos = nx.spring_layout(nx_graph)
    nx.draw(nx_graph, pos, with_labels=True, node_size=500, node_color='skyblue', edge_color='gray', width=2, alpha=0.6)
    edge_labels = nx.get_edge_attributes(nx_graph, 'weight')
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels)
    plt.show()

    nn = NearestNeighbor(graph)
    path, total_distance = nn.linear_search(start="E")
    print("\nChemin trouvé :", path)
    print("Distance totale :", total_distance)


if __name__ == "__main__":
    main()
