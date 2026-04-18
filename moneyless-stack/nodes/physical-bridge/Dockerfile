FROM python:3.11-slim
WORKDIR /app
COPY bridge.py /app/bridge.py
USER 65534:65534
CMD ["python", "-u", "/app/bridge.py"]
