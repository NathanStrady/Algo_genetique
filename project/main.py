import networkx as nx
from matplotlib import pyplot as plt

from project.graph import Graph
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

    print(graph)
    G = graph.to_nx_graph()

    pos = nx.spring_layout(G)  # Disposition des noeuds
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10)
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)
    plt.show()

    nn = NearestNeighbor(graph)
    path, total_distance = nn.linear_search(start="D")
    print("\nChemin trouvé :", path)
    print("Distance totale :", total_distance)


if __name__ == "__main__":
    main()
