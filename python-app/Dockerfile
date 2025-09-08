FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Create a writable .streamlit config directory
RUN mkdir -p /app/.streamlit && chmod -R 777 /app/.streamlit

# Tell Streamlit to use this folder instead of "/.streamlit"
ENV STREAMLIT_CONFIG_DIR=/app/.streamlit
ENV STREAMLIT_BROWSER_GATHERUSAGESTATS=false

EXPOSE 8501

# Run streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501", "--server.baseUrlPath=/python", "--server.headless=true"]

