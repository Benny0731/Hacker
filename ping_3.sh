#!/bin/bash  
if [ "$#" -ne 1 ];then  
  echo "Usage - ./ping.sh [interface]"  
  echo "Excample - ./ping.sh 192.168.1.0"  
  echo "Example will perform an ARP scan of the local subnet to which eth0 is assigned"  
  exit  
fi  
  
prefix=$(echo $1 | cut -d '.' -f 1-3)  
  
for addr in $(seq 1 254);do  
   ping -c 1 $prefix.$addr | grep "bytes from" | cut -d " " -f 4 | cut -d ":" -f 1 &
done