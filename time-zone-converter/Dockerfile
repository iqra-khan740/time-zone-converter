# Start from a lightweight Python image
FROM python:3.12-slim

# Prevent Python from writing .pyc files & enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install system dependencies (safe for pip builds)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install
COPY Backend/requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy everything (Backend + frontend + Procfile)
COPY . /app/


# Expose port (platforms like Railway/Cloud Run set $PORT)
EXPOSE 8080

# Run with Gunicorn in production
# ${PORT:-8080} means: use env $PORT if exists, else default 8080
#CMD ["sh", "-c", "gunicorn -b 0.0.0.0:${PORT:-8080} Backend.app:app"]
CMD gunicorn -b 0.0.0.0:${PORT:-8080} Backend.app:app

