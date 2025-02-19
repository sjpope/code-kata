FROM python:3.9-slim
ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY . /app

CMD ["python", "generate.py"]