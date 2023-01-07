FROM python:3.11.1-slim

WORKDIR /code

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . /code

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]