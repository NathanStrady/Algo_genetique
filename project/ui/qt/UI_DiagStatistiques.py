from PyQt6 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt6.QtGui import QPixmap

class Ui_Dialog(object):
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

        # Créez les graphiques à l'ouverture du Dialog
        self.create_plots()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Statistiques TSP"))

    def create_plots(self):
        fig1 = Figure()
        ax1 = fig1.add_subplot(111)
        ax1.plot([0, 1, 2, 3], [0, 1, 4, 9], label='Parabole')
        ax1.set_title('Graphique 1')
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        ax1.legend()

        fig2 = Figure()
        ax2 = fig2.add_subplot(111)
        ax2.plot([0, 1, 2, 3], [0, -1, -4, -9], label='Inversé')
        ax2.set_title('Graphique 2')
        ax2.set_xlabel('X')
        ax2.set_ylabel('Y')
        ax2.legend()

        self.add_plot_to_graphics_view(fig1, self.graphicsView)
        self.add_plot_to_graphics_view(fig2, self.graphicsView_2)

    def add_plot_to_graphics_view(self, fig, graphics_view):
        canvas = FigureCanvas(fig)
        canvas.draw()

        image_path = 'temp_plot.png'
        canvas.print_figure(image_path, dpi=100)


        pixmap = QPixmap(image_path)

        scene = QtWidgets.QGraphicsScene(graphics_view)
        graphics_view.setScene(scene)
        scene.addPixmap(pixmap)

