FROM python:3.13-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

EXPOSE 80

# Run streamlit
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=80", "--server.baseUrlPath=/python", "--server.headless=true"]

