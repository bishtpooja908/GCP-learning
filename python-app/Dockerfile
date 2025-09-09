FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create a writable .streamlit config directory
RUN mkdir -p /app/.streamlit /app/.cache && chmod -R 777 /app

# Create a non-root user and set HOME
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
USER appuser
ENV HOME=/app

# Force Streamlit to use these paths
ENV STREAMLIT_CACHE_DIR=/app/.cache
ENV XDG_CONFIG_HOME=/app/.streamlit
ENV STREAMLIT_BROWSER_GATHERUSAGESTATS=false

EXPOSE 8501

# Run streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.baseUrlPath=/python", "--server.headless=true"]

# test