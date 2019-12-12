#!/bin/bash
  
if [ "$#" -ne 1 ]; then
	echo "Usage - ./UDP_hping.sh [/24 network address]"
	echo "Example - ./UDP_hping.sh 172.16.36.0"
	echo "Example will perform an UDP ping scan of the 172.16.36.0/24 network and output to an output.txt file"
	exit
fi
  
prefix=$(echo $1 | cut -d '.' -f 1-3)
  
for addr in $(seq 1 254); do
	hping3 $prefix.$addr --udp -c 1 >> r.txt;
done

grep Unreachable r.txt | cut -d " " -f 5 | cut -d "=" -f 2  >> output.txt
rm r.txt