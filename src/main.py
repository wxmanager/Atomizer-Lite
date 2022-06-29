from imports import *
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import *

def mainwin():
  
    

  app = QApplication([])
  app.setApplicationName("Atomizer - " + "")
  appwin = QWidget()
  
  appwin.setMinimumSize(QSize(500, 200))
  appwin.show()

  textedit = QTextEdit()
  textedit.setLineWrapMode(QTextEdit.LineWrapMode.NoWrap)
  textedit.setFont(QFont("Monospace"))

  savebutton = QPushButton("Save")
  savebutton.clicked.connect(lambda: QFileDialog.getSaveFileName(None, "Save File", "", "Atomizer Files (*.atomize)")) 
  
  def open():
    QFileDialog.getOpenFileName(None, "Open Atomizer file", "", "Atomizer Files (*.atomize)")
    textedit.setText(open)

  openbutton = QPushButton("Open")
  openbutton.clicked.connect(lambda: open() )
  




  


  winlayout = QVBoxLayout()
  
  winlayout.addWidget(textedit)
  winlayout.addWidget(savebutton)
  winlayout.addWidget(openbutton)
  appwin.setLayout(winlayout)
  
  appwin.show()

  app.exec()

if __name__ == '__main__':
  mainwin()
  