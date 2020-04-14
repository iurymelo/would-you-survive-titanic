FROM python:3.7.2-stretch

COPY . /home/app
WORKDIR /home/app

RUN pip install -r requirements.txt

CMD ["uwsgi", "app.ini"]
