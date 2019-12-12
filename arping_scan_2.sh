#!/bin/bash

if [ "$#" -ne 1 ];then       #-ne 1 参数不等于为1  
	echo "Usage - ./arping.sh [interface]"  
	echo "Excample - ./arping.sh eth0"  
	echo "Example will perform an ARP scan of the local subnet to which eth0 is assigned"  
	exit  
fi  
  
interface=$1             #输入的一个值，，赋值给interface变量  
# prefix=$(ifconfig $interface | grep "inet addr" | cut -d ':' -f 2 | cut -d ' ' -f 1 | cut -d '.' -f 1-3)
prefix=$(ifconfig $interface | grep "inet " | cut -d 't' -f 2 | cut -d '.' -f 1-3)

for addr in $(seq 1 254); do
	# arping -c 1 $prefix.$addr | grep "bytes from" | cut -d" " -f 5 | cut -d "(" -f 2 | cut -d")" -f 1
	arping -c 1 -I $1 $prefix.$addr | grep "reply from" | cut -d " " -f 4
done
