import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from uis.Ui_MainWindow import Ui_MainWindow


class MainWindow:
    def __init__(self) -> None:
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        self.ui.actionQuit.triggered.connect(self.main_win.close)
        self.ui.actionLoad_File.triggered.connect(self.load_file)
        self.ui.actionSave_file.triggered.connect(self.save_file)

    def show(self) -> None:
        self.main_win.show()

    def load_file(self):
        load_dlg = QFileDialog()
        f_name = load_dlg.getOpenFileName(load_dlg, caption="Load File")
        if not f_name[0] == "":
            with open(f_name[0], "r") as f:
                text = f.read()
                self.ui.plainTextEdit.setPlainText(text)

    def save_file(self):
        save_dlg = QFileDialog()
        f_name = save_dlg.getSaveFileName(save_dlg, caption="Save File")
        if not f_name[0] == "":
            with open(f_name[0], "w") as f:
                f.write(self.ui.plainTextEdit.toPlainText())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
