FROM python:3.8

WORKDIR /fastapi

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./app ./app

CMD ["python3", "./app/main.py"]