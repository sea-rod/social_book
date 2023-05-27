FROM python:alpine

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /social_book

COPY . /social_book/

RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000