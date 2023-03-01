FROM python:3

#update
RUN apt-get update

#install requirements
COPY ./requirements.txt /tmp/requirements.txt
WORKDIR /tmp
RUN pip3 install -r requirements.txt

#copy app
COPY . /authentication
WORKDIR /

CMD ["gunicorn", "-w", "3", "-b", ":5000", "-t", "360", "--reload", "user.wsgi:app"]