from imports import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont


def selectedfile():
  filename = QFileDialog.getOpenFileName()
  return filename

filename = "test"

def mainwin():
  app = QApplication([])
  app.setApplicationName("Atomizer - " + filename)
  appwin = QWidget()
  
  appwin.setMinimumSize(QSize(500, 200))
  appwin.show()

  textedit = QTextEdit()
  textedit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
  textedit.setFont(QFont("Monospace"))

  winlayout = QVBoxLayout()
  winlayout.addWidget(textedit)
  appwin.setLayout(winlayout)
  
  appwin.show()

  app.exec()

if __name__ == '__main__':
  mainwin()
  