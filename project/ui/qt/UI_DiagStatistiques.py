import networkx as nx
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore, QtWidgets

from project.Utils.drawing import plot_best_path
from project.geneticAlgorithm import GeneticAlgorithm
from project.graph import Graph


class Ui_Dialog(object):

    def __init__(self):
        self.nb_nodes = None
        self.nb_max_weigth = None
        self.num_generations = None
        self.num_individuals = None
        self.strategy = None
        self.strategy_init = None
        self.G = None

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(766, 453)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setStyleSheet("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView = QtWidgets.QGraphicsView(parent=Dialog)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.graphicsView_2 = QtWidgets.QGraphicsView(parent=Dialog)
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.gridLayout.addWidget(self.graphicsView_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Statistiques TSP"))

    def configure(self, nb_nodes, nb_max_weight, num_generations, num_individuals, strategy, strategy_init):
        # Assurez-vous que les paramètres sont valides
        if nb_nodes <= 0 or nb_max_weight <= 0 or num_generations <= 0 or num_individuals <= 0:
            raise ValueError("Les paramètres doivent être positifs et non nuls.")

        self.num_generations = num_generations
        self.num_individuals = num_individuals
        self.strategy = strategy
        self.strategy_init = strategy_init
        self.nb_nodes = nb_nodes
        self.nb_max_weigth = nb_max_weight
        self.G = Graph.generate_random_graph(self.nb_nodes, self.nb_max_weigth)

        self.startGA()

    def startGA(self):
        GA = GeneticAlgorithm(self.G)
        if (self.strategy_init == "Aléatoire"):
            best = GA.ga_tournament_random_search(self.num_individuals, self.num_generations,
                                              self.update_display_at_generation)
        else:
            best = GA.ga_tournament_linear_search(self.num_individuals, self.num_generations,
                                              self.update_display_at_generation)

    def update_display_at_generation(self, G, generation, best_path, fitness):

        self.plot_best_path(G, generation, best_path, self.graphicsView)
        self.plot_fitness(fitness, self.graphicsView_2)

        strategy_info = f"Séléction: {self.strategy} / Initialisation: {self.strategy_init}"
        generation_info = f"Génération: {generation} / Nb Individus par génération: {self.num_individuals}"
        fitness_info = f"Résultat: {fitness[-1] if len(fitness) > 0 else 'N/A'}"

        stats_text = (f"{generation_info}\n"
                      f"{strategy_info}\n"
                      f"{fitness_info}\n")


        self.label.setText(stats_text)

    def plot_best_path(self, G, generation, best_path, graphics_view):
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)

        pos = nx.spring_layout(G, seed=42)

        ax.set_title(f'Meilleur chemin')

        start_node = best_path[0]
        node_colors = ['red' if node == start_node else 'skyblue' for node in G.nodes()]

        nx.draw(G, pos, with_labels=True, node_size=500, node_color=node_colors, edge_color='none', ax=ax)
        path_edges = [(best_path[i], best_path[i + 1]) for i in range(len(best_path) - 1)]
        path_edges.append((best_path[-1], best_path[0]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2, ax=ax,
                               arrows=True, arrowstyle='-|>', arrowsize=10)
        self.add_plot_to_graphics_view(fig, graphics_view)

    def plot_fitness(self, fitness_values, graphics_view):
        fig = Figure(figsize=(10, 6))
        ax = fig.add_subplot(111)
        print(fitness_values)

        ax.plot(range(1, len(fitness_values) + 1), fitness_values, color='blue', marker='o')
        ax.set_title("Évolution de la Fitness")
        ax.set_xlabel("Génération")
        ax.set_ylabel("Fitness")

        ax.set_ylim(0, max(fitness_values))
        self.add_plot_to_graphics_view(fig, graphics_view)

    def add_plot_to_graphics_view(self, fig, graphics_view):
        canvas = FigureCanvas(fig)
        canvas.draw()

        image_path = './project/plots/graph_plot.png'
        canvas.print_figure(image_path, dpi=100)

        pixmap = QPixmap(image_path)

        scene = QtWidgets.QGraphicsScene(graphics_view)
        graphics_view.setScene(scene)
        scene.addPixmap(pixmap)
