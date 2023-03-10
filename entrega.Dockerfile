FROM ubuntu:20.04
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y python3

RUN apt-get install -y python3-pip

COPY requirements.txt /opt/
RUN pip3 install -r /opt/requirements.txt

WORKDIR /opt
CMD [ "flask", "--app", "./entregadelosalpes/entrega/app.py", "--debug", "run", "--host=0.0.0.0"]
