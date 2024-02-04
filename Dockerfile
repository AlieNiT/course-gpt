# Use an official Python runtime as a parent image
FROM python:3.10

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

# Expose the port that Django will run on
EXPOSE 9000

# Run Django when the container launches
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
