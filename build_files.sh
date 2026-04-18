#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "--- Build Starting ---"

# Install dependencies
echo "Installing dependencies..."
python3 -m pip install -r requirements.txt

# Create static directory if it doesn't exist
mkdir -p staticfiles_build/static

# Collect static files
echo "Collecting static files..."
# Using --no-input and --clear to ensure a clean build
python3 manage.py collectstatic --no-input --clear

echo "--- Build Finished ---"
