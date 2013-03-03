import sock
import select
import sys

class IRC:
	nick = ''
	user = ''
	servers = {}
	inputs = []
	outputs = []
	event_queue = []
	
	def __init__(self, nick, user):
		self.user = user
		self.nick = nick
	
	def add_server(self, server_nick, server_name, port):
		self.servers[server_nick] = sock.MySocket(server_name, port, server_nick)
	
	def register(self):
		for key in self.servers:
			self.servers[key].send_queue.append(': NICK '+self.nick+'\r\n')
			self.servers[key].send_queue.append(': USER '+self.user+ ' 0 * :Mr Hamster\r\n')		

	def handle_connection(self):
			ready_to_read, ready_to_write, in_error = select.select(self.servers.values(), self.servers.values(), [])
			
			for s in ready_to_read:
				msg = s.recv()
				self.event_queue.append( (msg, s.name) )
				print(msg)
			
			for s in ready_to_write:
				s.send()
				
			#Handle all received messages
			for event in self.event_queue:
				msg_to_handle, _ = self.event_queue.pop()

				words = msg_to_handle.split(' ');
				#Reply to ping
				if words[0] == 'PING':
					self.servers[event[1]].send('PONG '+words[1])
					self.servers[event[1]].send(": JOIN #teamliquid\r\n")					
			
			