import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction
from uis.Ui_MainWindow import Ui_MainWindow


class MainWindow:
    def __init__(self) -> None:
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.actionQuit.triggered.connect(self.main_win.close)

    def show(self) -> None:
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
