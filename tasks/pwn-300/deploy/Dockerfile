FROM ubuntu:bionic

RUN apt-get update
RUN apt-get install -y python3 ucspi-tcp

RUN useradd pwn
RUN passwd -d pwn
COPY pwn.py /
COPY flag.txt /
RUN chmod +x pwn.py
RUN chmod 744 flag.txt

EXPOSE 2201
USER pwn
CMD tcpserver -t 50 -RHl10 0.0.0.0 2201 ./pwn.py
