<<<<<<< HEAD
FROM python:3.10-slim
=======
FROM python:3.11-slim
>>>>>>> qa

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

<<<<<<< HEAD
COPY . .
COPY static /app/static
=======
COPY app/ ./app
COPY static/ ./static
>>>>>>> qa

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8003"]
