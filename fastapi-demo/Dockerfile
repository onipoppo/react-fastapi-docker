FROM python:3.10

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["gunicorn", "main:app", "--workers 4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]