# Use official Python image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your project files into the image
COPY . .

# Install dependencies (build.sh handles this)
RUN chmod +x /app/build.sh
RUN /app/build.sh

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Expose Django port
EXPOSE 8000

# Use entrypoint.sh to run commands
CMD ["/app/entrypoint.sh"]
