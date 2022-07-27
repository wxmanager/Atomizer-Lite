from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

class Window(QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle("Atomizer")
    self.setGeometry(100, 100, 800, 600)    
    self.setMinimumSize(QSize(200, 200))
    self.show()

    txt = QTextEdit()
    txt.setFont(QFont("Monospace"))

    def file_save(self):
      name = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt)")
      file = open (name, "w")
      text = self.txt.toPlainText()
      file.write(text)
      file.close()
    
    menubar = self.menuBar()
    fileMenu = menubar.addMenu('&File')

    saveFile = QAction("&Save File", self)
    saveFile.setShortcut("Ctrl+S")
    saveFile.setStatusTip('Save File')
    saveFile.triggered.connect(self, file_save)

    
    fileMenu.addAction(saveFile)

    winlayout = QVBoxLayout()
    winlayout.setContentsMargins(15,15,15,15)


    winlayout.addWidget(txt)
    self.setLayout(winlayout)
    
    self.show()

    app = QApplication(sys.argv)
    


def run():
  app = Window()

  sys.exit(app.exec_())

  
  

run()
  

