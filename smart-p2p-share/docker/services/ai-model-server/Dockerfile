FROM python:3.11-slim

WORKDIR /app

COPY ../../../../ai/service/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY ../../../../ai/service/ ./

EXPOSE 8501

CMD ["python", "main.py"]
