# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your project files into the image
COPY . .

# Install dependencies (build.sh handles this)
RUN chmod +x /app/build.sh
RUN /app/build.sh

# Expose Django port
EXPOSE 8000

# Run migrations & start server at container start time
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
