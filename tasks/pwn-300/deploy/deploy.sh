#!/bin/bash

if [ `whoami` != "root" ]; then
	echo "Must be root."
	exit
fi

if [ $1 = "-b" ]; then
	docker build . -t pwn-300 
fi
docker kill pwn-300
docker rm pwn-300
docker run -d --name=pwn-300 -p 0.0.0.0:13337:2201 pwn-300

while true; do
	sleep 150  
	echo "pwn-300 reset"
	docker kill pwn-300
	docker rm pwn-300
	docker run -d --name=pwn-300 -p 0.0.0.0:13337:2201 pwn-300
done
