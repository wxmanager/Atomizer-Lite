import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PyQt5 import QtCore, QtGui
from uis.Ui_MainWindow import Ui_MainWindow
import os


class MainWindow:
    def __init__(self) -> None:
        self.aboutdlg = None
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        font = QtGui.QFont('monospace')
        font.setPointSize(15)

        self.ui.plainTextEdit.setFont(font)

        self.main_win.setWindowTitle("Atomizer - New File")
        self.ui.actionQuit.triggered.connect(self.main_win.close)
        self.ui.actionLoad_File.triggered.connect(self.load_file)
        self.ui.actionSave_file.triggered.connect(self.save_file)
        self.ui.actionAbout.triggered.connect(self.about)

    def show(self) -> None:
        self.main_win.show()

    def load_file(self):
        load_dlg = QFileDialog()
        f_name = load_dlg.getOpenFileName(load_dlg, caption="Load File")

        if not f_name[0] == "":
            with open(f_name[0], "r") as f:
                text = f.read()
                self.ui.plainTextEdit.setPlainText(text)
                self.main_win.setWindowTitle(f"Atomizer - {f_name[0]}")

    def save_file(self):
        save_dlg = QFileDialog()
        f_name = save_dlg.getSaveFileName(save_dlg, caption="Save File")
        if not f_name[0] == "":
            with open(f_name[0], "w") as f:
                f.write(self.ui.plainTextEdit.toPlainText())
                self.main_win.setWindowTitle(f"Atomizer - {f_name[0]}")

    def about(self):
        self.aboutdlg = QMessageBox()
        self.aboutdlg.setIcon(QMessageBox.Information)
        self.aboutdlg.setWindowTitle("About Atomizer")
        self.aboutdlg.setText(
            "Atomizer is atext editor made for the Wxmanager Desktop environment \n\nAtomizer Version: ")
        self.aboutdlg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
