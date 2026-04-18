FROM python:3.11-slim
WORKDIR /app
COPY consensus.py /app/consensus.py
USER 65534:65534
CMD ["python", "-u", "/app/consensus.py"]
