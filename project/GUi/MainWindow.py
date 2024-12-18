from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QHBoxLayout, QFrame, QWidget, QSpinBox
from project.GUi.Widgets.Color import Color


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Recherche TSP - Algorithme Génétique")

        pageLayout = QVBoxLayout()
        vertical_layout = QVBoxLayout()
        frame_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        pageLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        horizontal_layout2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        horizontal_layout2.setSpacing(30)
        vertical_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        frame_layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Titre
        title = QLabel("Recherche Mathématique sur les Algorithmes Génétiques - Travelling Salesman Problem (TSP)")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 18pt; font-weight: bold; ")

        # Sous-titre pour les options
        subtitle = QLabel("Options pour l'Algorithme Génétique")
        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        subtitle.setStyleSheet("font-size: 15pt; font-weight: bold; ")

        frame = QFrame()
        frame.setFrameShape(QFrame.Shape.Box)
        frame.setFrameShadow(QFrame.Shadow.Plain)

        num_individuals_label = QLabel("Nombre d'individus par génération :")
        num_individuals_input = QSpinBox()
        num_individuals_input.setRange(1, 1000)

        num_generations_label = QLabel("Nombre de générations :")
        num_generations_input = QSpinBox()
        num_generations_input.setRange(1, 1000)

        frame.setLayout(frame_layout)

        # Organisation dans les layouts
        pageLayout.addWidget(title)
        horizontal_layout.addWidget(frame)
        vertical_layout.addWidget(subtitle)
        horizontal_layout2.addWidget(num_generations_label)
        horizontal_layout2.addWidget(num_generations_input)
        horizontal_layout2.addWidget(num_individuals_label)
        horizontal_layout2.addWidget(num_individuals_input)


        pageLayout.addLayout(horizontal_layout, stretch=1)
        horizontal_layout.addLayout(vertical_layout)
        vertical_layout.addLayout(horizontal_layout2)

        widget = QWidget()
        widget.setLayout(pageLayout)
        self.setCentralWidget(widget)
