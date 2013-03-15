import irc
import sys
import gui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

app = QApplication(sys.argv)
mainWindow = gui.MainWindow()
mainWindow.show()

app.exec_()