FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for MySQL and building packages
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Flask application code
COPY . /app/

# Expose the Flask port
EXPOSE 5000

# Point FLASK_APP to the WSGI entrypoint (used by Flask CLI)
ENV FLASK_APP=wsgi.py
ENV FLASK_RUN_HOST=0.0.0.0

# Start the app using Gunicorn, serving the "app" object in wsgi.py
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
