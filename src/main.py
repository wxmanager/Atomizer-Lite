from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *

def mainwin():
  
  app = QApplication([])
  app.setApplicationName("Atomizer")
  appwin = QWidget()
  
  appwin.setMinimumSize(QSize(500, 200))
  appwin.show()

  textedit = QTextEdit()
  textedit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
  textedit.setFont(QFont("Monospace"))

  winlayout = QVBoxLayout()
  winlayout.setContentsMargins(0,0,0,0)
  
  winlayout.addWidget(textedit)
  appwin.setLayout(winlayout)
  
  appwin.show()

  app.exec()

if __name__ == '__main__':
  mainwin()
  