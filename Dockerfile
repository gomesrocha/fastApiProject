FROM python:3.8.10-alpine
LABEL maintainer = "Fabio Gomes Rocha <gomesrocha@gmail.com>"
WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends gcc

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt


COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]