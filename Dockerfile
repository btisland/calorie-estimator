FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml uv.lock* ./
COPY src ./src
COPY .env.example ./.env

# Install uv package manager
RUN pip install --no-cache-dir uv

# Install dependencies
RUN uv sync --no-dev

# Expose port
EXPOSE 8501

# Set environment variables for Streamlit
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true
ENV STREAMLIT_LOGGER_LEVEL=info

# Run the app
CMD ["streamlit", "run", "src/app.py"]
