FROM python:3.12-slim

WORKDIR /app

COPY config /app/config
COPY kamal /data/kamal
COPY app.py /app/app.py
COPY requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "app.py"]