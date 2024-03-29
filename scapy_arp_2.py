#!/usr/bin/python  

import logging 
import subprocess  
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)  
from scapy.all import*                             

if len( sys.argv ) !=2: 
    print "Usage - ./arp_discpy [interface]"  
    print "Example - ./arp_disc.py eth0"  
    print "Example will perform an ARP scan of thr local subnet to which eth0 is assigned"  
    sys.exit()  

interface = str(sys.argv[1])  

# ip=subprocess.check_output("ifconfig "+interface+" | grep 'inet addr' | cut -d ':' -f 2 |cut -d ' ' -f 1",shell=True).strip()  
ip=subprocess.check_output("ifconfig "+interface+" | grep 'inet ' | cut -d 't' -f 2 | cut -d '.' -f 1-3",shell=True).strip()  
prefix = ip.split(".")[0] + '.' + ip.split(".")[1] + '.' + ip.split(".")[2] + '.'  

for addr in range(0,254):  
    answer=sr1(ARP(pdst=prefix+str(addr)),timeout=0.1,verbose=0)
    if answer ==None:  
        pass;  
    else:  
        print prefix+str(addr)
