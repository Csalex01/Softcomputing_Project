FROM tensorflow/tensorflow:latest

RUN apt update
RUN apt upgrade -y

RUN pip install matplotlib

CMD [ "/bin/bash" ]