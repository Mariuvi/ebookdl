from PyQt4.QtCore import *
from PyQt4.QtGui import *
import irc

class MainWindow(QDialog):

	def __init__(self, parent = None):
		super(MainWindow, self).__init__(parent)
		
		self.checkbox_undernet = QCheckBox('#Ebooks')
		self.checkbox_irchighway = QCheckBox('#bookz')
		self.connectButton = QPushButton('Connect')
		self.msg_list = QListWidget()
		
		grid = QGridLayout()
		
		self.setLayout(grid)
		grid.addWidget(self.checkbox_irchighway, 0, 1)
		grid.addWidget(self.checkbox_undernet, 1, 1)
		grid.addWidget(self.connectButton, 2, 1)
		grid.addWidget(self.msg_list, 3, 1)
		self.setWindowTitle('Ebook downloader')
		
			
		self.connect(self.connectButton, SIGNAL('clicked()'), self.setup_connection)
		
		self.show()
		
	def setup_connection(self):
		self.irc = irc.IRC('Mr Hamster', 'Maraaaraka')
		
		if self.checkbox_undernet.isChecked():
			self.irc.add_server("undernet", "Budapest.HU.EU.UnderNet.org", 6667)
		if self.checkbox_irchighway.isChecked():
			self.irc.add_server("irchighway", "irc.irchighway.net", 6667)
			
		self.irc.register()
		self.connect(self.irc, SIGNAL('msg_received(PyQt_PyObject)'), self.display_msg)
		self.irc.start()
		
	def display_msg(self, msg):
		self.msg_list.addItem(' '.join(msg))
		
		