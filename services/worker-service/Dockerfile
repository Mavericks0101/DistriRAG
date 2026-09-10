FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy package metadata and application source code
COPY pyproject.toml README.md ./
COPY app/ ./app/

# Install the service and its dependencies
RUN pip install --no-cache-dir .

# Run worker process
CMD ["python", "-m", "app.worker"]
