# FROM tensorflow/tensorflow:latest
FROM    ubuntu:latest

RUN     apt-get update -y
RUN     apt-get upgrade -y

RUN     apt-get install -y python3 python3.12-venv

RUN     python3 -m venv env

CMD     [ "/bin/bash" ]
