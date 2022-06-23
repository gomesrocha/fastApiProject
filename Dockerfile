FROM python:3.8.10-alpine
LABEL maintainer = "Fabio Gomes Rocha <gomesrocha@gmail.com>"
WORKDIR /app

RUN python -m pip install --upgrade pip

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
EXPOSE 8080
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

