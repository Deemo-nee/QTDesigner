import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from platform import Ui_MainWindow
from PyQt5.QtCore import QFile, QTextStream
from PyQt5.QtWidgets import QApplication


class MainWindow:
    def __init__(self):
        self.main_win = QMainWindo5w()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
