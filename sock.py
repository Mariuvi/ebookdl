import socket

class MySocket(object):
	
	name = ''
	sock = None
	send_queue = []
	
	def __init__(self, ip, port, name):
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((ip, port))
		self.sock.setblocking(0)
		self.name = name
		
	def send(self):
		for msg in self.send_queue:
			totalsent = 0
			while totalsent < len(msg):
				sent = self.sock.send(msg[totalsent:].encode())
				if sent == 0:
					raise RunTimeError("socket connection broken")
				totalsent += sent
			print("Sent "+msg+"\n")
		self.send_queue = []	
		
	def recv(self):
		msg = ""
		while (True):
			char = self.sock.recv(1).decode()
			if char == "\n":
				msg+=char
				break;
			else:
				msg+=char			
		return msg
		
	def fileno(self):
		return self.sock.fileno()