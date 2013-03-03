import IRC

irc = IRC.IRC('MrHamster', 'Mad dog')
irc.add_server("quake", "irc.quakenet.org", 6667)
irc.register()
while(True):
	irc.handle_connection()
print("end\n")