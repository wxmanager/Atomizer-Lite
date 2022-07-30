from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
import sys

class MainWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Atomizer")

    self.mainatomizer = Atomizer()
    self.setCentralWidget(self.mainatomizer)
    

    saveaction = QAction("&Save File (Non Functional)", self)
    saveaction.setShortcut("Ctrl+S")
    saveaction.setStatusTip('Save File')
    saveaction.triggered.connect(qApp.quit)
    
    openaction = QAction("&Open File (Non Functional)", self)
    openaction.setShortcut("Ctrl+O")
    openaction.setStatusTip('Open File')
    openaction.triggered.connect(qApp.quit)

    exitaction = QAction('&Exit', self)
    exitaction.setShortcut('Ctrl+Q')
    exitaction.setStatusTip('Exit Atomizer')
    exitaction.triggered.connect(qApp.quit)
    
    abtqt = QAction('&About QT', self)
    abtqt.setStatusTip('About QT')
    abtqt.triggered.connect(qApp.aboutQt)

  
    
    self.statusBar()

    bar = self.menuBar()
    
    fileMenu = bar.addMenu("&File")
    fileMenu.addAction(saveaction)
    fileMenu.addAction(openaction)
    fileMenu.addAction(exitaction)

    aboutMenu = bar.addMenu("&About")
    aboutMenu.addAction(abtqt)

class Atomizer(QtWidgets.QWidget):
  def __init__(self):
    super().__init__()

    self.setWindowTitle("Atomizer")
    self.setGeometry(100, 100, 800, 600)    
    self.setMinimumSize(QSize(500, 400))

    txt = QTextEdit()
    txt.setFont(QFont("Monospace"))
    
    winlayout = QVBoxLayout()
    winlayout.setContentsMargins(15,15,15,15)

    winlayout.addWidget(txt)
    self.setLayout(winlayout)


if __name__ == '__main__':
  app = QtWidgets.QApplication([])

  widget = MainWindow()
  widget.show()

  sys.exit(app.exec())
