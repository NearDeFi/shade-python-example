FROM python:3.11-alpine

WORKDIR /app

# Install system dependencies
RUN apk add --no-cache gcc musl-dev

# Copy toml file
COPY pyproject.toml .

# Install dependencies
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