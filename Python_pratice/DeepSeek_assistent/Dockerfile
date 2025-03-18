FROM python:3.10-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    espeak \
    ffmpeg \
    tk \
    kbd \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Дополнительная установка keyboard (если нужно отдельно)
RUN pip install keyboard
RUN apt-get update && apt-get install -y \
    tesseract-ocr \
    espeak \
    ffmpeg \
    tk \
    kbd \
    && rm -rf /var/lib/apt/lists/*
# Copy application code
COPY . /app

# Run the application
CMD ["python", "app.py"]