# Use official Python image
FROM python:3.11-slim

# Install work directory inside container
WORKDIR /app

# Copy file with requirements
COPY requirements.txt .

# Instal requirements
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project
COPY . .

# Indicate command for launch FastAPI
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]

