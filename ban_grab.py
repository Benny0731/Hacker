#!/usr/bin/python
import socket
import select
import sys

if len(sys.argv) != 4
	print "Usage - ./ban_grab.py [Target-IP] [First Port] [Last Port]"
	print "Example - ./ban_grab.py 172.16.36.25 1 100"
	print "Example will grab banners for TCP ports 1 through 100 on 192.168.36.25"
	sys.exit()
	
ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3]) 

for port in range(start,end):
	try:
		bangrab = socket_socket(socket.AF_INET, socket.SOCK_STREAM)
		bangrab.connect((ip.port))
		ready = select.select([bangrab].[][].1)
		
		if ready[0]:
			print "TCP Port " + str(port) + "-" + bangrab.recv(4096)
			bangrab.close()
	except:
		pass