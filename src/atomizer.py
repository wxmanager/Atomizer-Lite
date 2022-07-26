from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

def mainwin():
  
  app = QApplication([])
  app.setApplicationName("Atomizer")
  appwin = QWidget()
  
  appwin.setMinimumSize(QSize(200, 200))
  appwin.show()

  txt = QTextEdit()
  txt.setFont(QFont("Monospace"))

  winlayout = QVBoxLayout()
  winlayout.setContentsMargins(15,15,15,15)

  
  
  winlayout.addWidget(txt)
  appwin.setLayout(winlayout)
  
  appwin.show()

  app.exec()

if __name__ == '__main__':
  mainwin()
  