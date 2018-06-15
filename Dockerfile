FROM python:3

EXPOSE 8945
WORKDIR /app

COPY . /app

RUN pip install .\[deploy\]

ENTRYPOINT ["gunicorn", "--workers", "4", "--bind", "0.0.0.0:8945", "lidarrstats.app:app"]