# Use official Python 3.10 image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Install required packages

COPY requirements.txt .

RUN pip install -r requirements.txt

# Copy code into container
COPY . .

# Default command to run your pipeline (you can customize this)
CMD ["python", "pipeline.py"]