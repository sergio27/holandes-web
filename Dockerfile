FROM python:3.8

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

EXPOSE 8000

ENV AWS_DJANGO_KEY MY_SECRET_KEY
ENV AWS_HOST_URL *
ENV AWS_API_URL http://localhost:8000/api/

CMD python manage.py runserver 0.0.0.0:8000