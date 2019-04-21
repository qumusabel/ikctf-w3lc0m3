FROM ubuntu:bionic

RUN sudo apt update
RUN sudo apt install python3


RUN adduser service
COPY * / 
WORKDIR /

EXPOSE 1337
USER service
CMD tcpserver -t 50 -RHl10 0.0.0.0 1337 ./service.py