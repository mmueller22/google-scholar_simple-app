FROM python:3.12-slim as base

# Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Create app directory
WORKDIR /app

# Install system dependencies for lxml
RUN apt-get update && apt-get install -y \
    libxml2-dev \
    libxslt-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml ./
COPY scholar.py ./

# Development stage
FROM base as development

# Install development dependencies
RUN pip install -e .[dev]

# Create volume mount points
VOLUME ["/app", "/app/.scholar-cookies"]

# Set default command
CMD ["python", "scholar.py", "--help"]

# Production stage
FROM base as production

# Install only production dependencies
RUN pip install -e .

# Create non-root user for security
RUN useradd --create-home --shell /bin/bash scholar
USER scholar

# Create directory for cookie persistence
RUN mkdir -p /home/scholar/.scholar-cookies

# Set default command
CMD ["python", "scholar.py", "--help"]

# Testing stage
FROM development as testing

# Copy test files
COPY tests/ ./tests/

# Run tests by default
CMD ["pytest", "-v"]
