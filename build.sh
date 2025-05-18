#!/bin/bash

# Upgrade pip
pip install --upgrade pip

# Install dependencies (if using poetry or requirements.txt)
# If using poetry:
# pip install poetry && poetry config virtualenvs.create false && poetry install

# If using requirements.txt
pip install -r requirements.txt

# Collect static files (optional for production)
python manage.py collectstatic --noinput
