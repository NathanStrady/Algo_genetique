import networkx as nx
from project.graph import Graph
from project.geneticAlgorithm import GeneticAlgorithm

import sys
from PyQt6.QtWidgets import QApplication
from project.GUi.MainWindow import MainWindow

def start_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def main():
    # graph = Graph.generate_random_graph(15, 100)
    # GA = GeneticAlgorithm(graph)
    # GA.ga_tournament_random_search(50, 50)
    start_app()


if __name__ == "__main__":
    main()
