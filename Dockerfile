# Use a single stage to avoid virtual environment issues
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies from registry
COPY pyproject.toml .

# Install the shade-agent-py package from registry
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir shade-agent-py

# Copy the application code
COPY src/ ./src/

# Set production environment
ENV ENV=production

# Set working directory to where the app is
WORKDIR /app/src

# Run the application
CMD ["python", "app.py"]
