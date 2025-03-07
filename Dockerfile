FROM python:3.10-slim-buster

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .
WORKDIR /flask-app/blueprintapp

#RUN rm -rf migrations
RUN flask db init
RUN flask db migrate
RUN flask db upgrade

WORKDIR /flask-app/

CMD ["python3", "run.py"]