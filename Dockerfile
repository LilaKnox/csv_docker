FROM python:latest
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY csv_processing.py .
COPY airports.csv .

CMD ["python", "csv_processing.py"]
