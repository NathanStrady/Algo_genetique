# Form implementation generated from reading ui file 'project/ui/qt/mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from project.ui.qt.UI_DiagStatistiques import Ui_Dialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 473)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.spinBox_2 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_2.setMinimum(1)
        self.spinBox_2.setMaximum(1000)
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout_7.addWidget(self.spinBox_2)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_8.addWidget(self.label_3)
        self.spinBox_3 = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox_3.setMinimum(1)
        self.spinBox_3.setMaximum(1000)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_8.addWidget(self.spinBox_3)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.nombreDeGNRationLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.nombreDeGNRationLabel.setObjectName("nombreDeGNRationLabel")
        self.horizontalLayout_2.addWidget(self.nombreDeGNRationLabel)
        self.nombreDeGNRationSpinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.nombreDeGNRationSpinBox.setMinimum(1)
        self.nombreDeGNRationSpinBox.setMaximum(1000)
        self.nombreDeGNRationSpinBox.setObjectName("nombreDeGNRationSpinBox")
        self.horizontalLayout_2.addWidget(self.nombreDeGNRationSpinBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(parent=self.centralwidget)
        self.spinBox.setMinimum(1)
        self.spinBox.setMaximum(1000)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.choixDeLaStratGieDeGNRationDeDPartLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.choixDeLaStratGieDeGNRationDeDPartLabel.setObjectName("choixDeLaStratGieDeGNRationDeDPartLabel")
        self.horizontalLayout_5.addWidget(self.choixDeLaStratGieDeGNRationDeDPartLabel)
        self.choixDeLaStratGieDeGNRationDeDPartComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.choixDeLaStratGieDeGNRationDeDPartComboBox.setObjectName("choixDeLaStratGieDeGNRationDeDPartComboBox")
        self.choixDeLaStratGieDeGNRationDeDPartComboBox.addItem("")
        self.choixDeLaStratGieDeGNRationDeDPartComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.choixDeLaStratGieDeGNRationDeDPartComboBox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.choixDeLaStratGieLabel = QtWidgets.QLabel(parent=self.centralwidget)
        self.choixDeLaStratGieLabel.setObjectName("choixDeLaStratGieLabel")
        self.horizontalLayout_4.addWidget(self.choixDeLaStratGieLabel)
        self.choixDeLaStratGieComboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.choixDeLaStratGieComboBox.setObjectName("choixDeLaStratGieComboBox")
        self.choixDeLaStratGieComboBox.addItem("")
        self.choixDeLaStratGieComboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.choixDeLaStratGieComboBox)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 797, 33))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.pushButton.clicked.connect(self.on_button_click)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Algorithmes Génétiques - TSP"))
        self.label_2.setText(_translate("MainWindow", "Nb Noeud du graphe"))
        self.label_3.setText(_translate("MainWindow", "Poids max des arêtes"))
        self.nombreDeGNRationLabel.setText(_translate("MainWindow", "Nombre d\'individu par Générations : "))
        self.label.setText(_translate("MainWindow", "Nombre de Générations : "))
        self.choixDeLaStratGieDeGNRationDeDPartLabel.setText(_translate("MainWindow", "Choix de la stratégie d\'initialisation :"))
        self.choixDeLaStratGieDeGNRationDeDPartComboBox.setItemText(0, _translate("MainWindow", "Aléatoire"))
        self.choixDeLaStratGieDeGNRationDeDPartComboBox.setItemText(1, _translate("MainWindow", "Algorithme Glouton du plus proche voisin"))
        self.choixDeLaStratGieLabel.setText(_translate("MainWindow", "Choix de la stratégie"))
        self.choixDeLaStratGieComboBox.setItemText(0, _translate("MainWindow", "Tournois par sélection"))
        self.choixDeLaStratGieComboBox.setItemText(1, _translate("MainWindow", "Tournois par rang"))
        self.pushButton.setText(_translate("MainWindow", "Lancer"))

    def on_button_click(self):
        self.open_matplotlib_dialog()

    def open_matplotlib_dialog(self):
        num_generations = self.spinBox.value()
        num_individuals = self.nombreDeGNRationSpinBox.value()
        strategy = self.choixDeLaStratGieComboBox.currentText()
        strategy_init = self.choixDeLaStratGieDeGNRationDeDPartComboBox.currentText()
        nb_nodes = self.spinBox_2.value()
        nb_max_weight = self.spinBox_3.value()

        self.dialog = QtWidgets.QDialog()
        self.dialog_ui = Ui_Dialog()
        self.dialog_ui.setupUi(self.dialog)
        self.dialog_ui.configure(nb_nodes, nb_max_weight, num_generations, num_individuals, strategy, strategy_init)
        self.dialog.exec()