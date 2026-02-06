FROM python:3.14.3-alpine
ENV PYTHONBUFFERED=1
RUN pip install --upgrade pip
WORKDIR /visits-count
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY main.py .
ENTRYPOINT ["fastapi dev"]
CMD ["main.py"]