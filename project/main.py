from ui.MainWindow import MainWindow
import sys
from PyQt6.QtWidgets import QApplication

def start_app():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


def main():
    start_app()


if __name__ == "__main__":
    main()
