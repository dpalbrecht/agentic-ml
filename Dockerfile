FROM python:3.11-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

WORKDIR /project

# Start with common ML basics — commands will pip install more as needed
# and requirements.txt gets updated to track what's installed
COPY requirements.txt .
RUN uv pip install --system --no-cache -r requirements.txt

# Project gets mounted at /project at runtime
