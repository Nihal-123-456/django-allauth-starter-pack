#!/usr/bin/env bash
set -o errexit

# Navigate to the Django project directory
cd src

# Install Python dependencies from requirements.txt
pip install -r ../requirements.txt

# Run custom command to download Flowbite files
python manage.py download_vendor

# Collect static files for WhiteNoise
python manage.py collectstatic --no-input

# Apply database migrations for Neon PostgreSQL
python manage.py migrate