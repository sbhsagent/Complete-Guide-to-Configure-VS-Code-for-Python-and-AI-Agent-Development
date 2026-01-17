# Use Python 3.12 slim image
FROM python:3.12-slim

WORKDIR /app

# For security, create a non-root user
RUN addgroup --system appuser && adduser --system --ingroup appuser appuser

# Copy requirements first for better caching
COPY --chown=appuser:appuser requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY --chown=appuser:appuser . .

# Add health check (using Python instead of curl for slim image)
HEALTHCHECK --interval=30s --timeout=3s \
  CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

# Switch to the non-privileged user
USER appuser

# Expose port and define entry point for FastAPI
EXPOSE 8000
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
