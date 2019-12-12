#!/bin/bash  
if [ "$#" -ne 2 ];then  
  	echo "Usage - ./arping.sh [interface file]"  
  	echo "Excample - ./arping.sh eth0 file"  
  	echo "Example will perform an ARP scan of the local subnet to which eth0 is assigned"  
  	exit  
fi 
interface=$1
file=$2
for addr in $(cat $file);do  
   	#arping -c 1 $addr | grep "bytes from" | cut -d" " -f 5 | cut -d "(" -f 2 | cut -d")" -f 1  
	arping -c 1 -I $interface $addr | grep "reply from" | cut -d " " -f 4
done 
