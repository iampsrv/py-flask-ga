FROM python:3.10.0a4-buster
COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "ap.py"]
