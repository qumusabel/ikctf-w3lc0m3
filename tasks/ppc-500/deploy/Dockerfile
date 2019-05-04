FROM ubuntu:bionic

RUN apt-get update
RUN apt-get install -y python3 ucspi-tcp 

RUN useradd service -m
RUN passwd -d service
COPY service.py /
RUN chmod +x service.py 
WORKDIR /

EXPOSE 2200
USER service
CMD tcpserver -t 50 -RHl10 0.0.0.0 2200 ./service.py
