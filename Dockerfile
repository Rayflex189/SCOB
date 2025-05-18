FROM python:3.11

WORKDIR /app

COPY . .

# Ensure build.sh has execute permissions
RUN chmod 755 /app/build.sh

RUN /app/build.sh

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
