FROM python:3.14.3-alpine
ENV PYTHONBUFFERED=1
RUN pip install --upgrade pip
WORKDIR /visits-count
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
EXPOSE 8000
CMD ["fastapi", "dev", "main.py", "--host", "0.0.0.0", "--port", "8000"]