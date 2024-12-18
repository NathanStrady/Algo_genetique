import networkx as nx
from matplotlib import pyplot as plt

def plot_best_path(G, generation, best_path):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(10, 6))
    plt.title(f'Generation {generation + 1} - Best Path')

    start_node = best_path[0]
    node_colors = ['red' if node == start_node else 'skyblue' for node in G.nodes()]

    nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, edge_color='grey')

    path_edges = [(best_path[i], best_path[i + 1]) for i in range(len(best_path) - 1)]
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, arrows=True, arrowstyle='-|>',
                           arrowsize=10)

    nx.draw_networkx_edges(G, pos, edgelist=[(best_path[-1], best_path[0])], edge_color='red', width=2, arrows=True,
                           arrowstyle='-|>', arrowsize=10)

    plt.show()