# Use Python base image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy project files into container
COPY . .

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Make build.sh executable if it exists
RUN chmod +x build.sh

# Run build script (if needed)
RUN ./build.sh

# Expose the port your app runs on
EXPOSE 8000

# Command to run the app (adjust as needed)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
