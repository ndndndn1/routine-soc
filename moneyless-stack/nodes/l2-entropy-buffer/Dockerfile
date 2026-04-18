FROM python:3.11-slim
WORKDIR /app
COPY entropy_buffer.py /app/entropy_buffer.py
USER 65534:65534
CMD ["python", "-u", "/app/entropy_buffer.py"]
