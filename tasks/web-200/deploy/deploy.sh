#!/bin/bash

if [ `whoami` != "root" ]; then
	echo "Must be root."
	exit
fi

if [ $1 = "-b" ]; then
	docker build . -t web-200
fi
docker kill web-200
docker rm web-200
docker run -d --name=web-200 -p 0.0.0.0:81:80 web-200

while true; do
	sleep 150  
	echo "web-200 reset"
	docker kill web-200
	docker rm web-200
	docker run -d --name=web-200 -p 0.0.0.0:81:80 web-200
done
