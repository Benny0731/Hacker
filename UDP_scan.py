#!/usr/bin/python  
  
import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import*
import time
import sys

if len(sys.argv)!=4:
	print "Usage - ./UDP_scan.py [Target-IP] [First Port] [Last Port]"
	print "Example - ./UDP_scan.py 172.16.36.25 1 100"
	print "Example will UDP Port scan 1 through 100 on 192.168.36.25"
	sys.exit()
  
ip = sys.argv[1]
start = int(sys.argv[2])
end = int(sys.argv[3]) 
  
for port in range(start,end):  
	response=sr1(IP(dst=ip)/UDP(dport=port),timeout=1, verbose=0)  
	time.sleep(1) 
        if response == None:
	    print port
	else:
	    pass
