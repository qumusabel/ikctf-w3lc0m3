#!/bin/bash

if [ `whoami` != "root" ]; then
	echo "Must be root."
	exit
fi

if [ $1 = "-b" ]; then
	docker build . -t ppc-500 
fi
docker kill ppc-500
docker rm ppc-500
docker run -d --name=ppc-500 -p 0.0.0.0:1337:2200 ppc-500

while true; do
	sleep 150  
	echo "ppc-500 reset"
	docker kill ppc-500
	docker rm ppc-500
	docker run -d --name=ppc-500 -p 0.0.0.0:1337:2200 ppc-500
done
