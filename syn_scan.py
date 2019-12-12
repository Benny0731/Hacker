#!/usr/bin/python  
  
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*
import time
import sys

if len(sys.argv)!=4:
	print "Usage - ./syn_scan.py [Target-IP] [First Port] [Last Port]"
	print "Example - ./syn_scan.py 172.16.36.25 1 100"
	print "Example will TCP SYN scan Ports 1 through 100 on 192.168.36.25"
	sys.exit()
  
ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3]) 
  
for port in range(start,end):  
	response=sr1(IP(dst=ip)/TCP(dport=port),timeout=1, verbose=0)  
	if response == None:
	    pass
	else:
            if int(response[TCP].flags)==18:
		print port
            else:
		pass
