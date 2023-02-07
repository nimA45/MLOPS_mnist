FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV LISTEN_PORT=5000
EXPOSE 5000

CMD ["python","my_app.py"]


