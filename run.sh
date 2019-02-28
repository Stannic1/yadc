#!/bin/bash

# This run script handles starting the localhost server for the Django project.
echo "Starting the Django web application locally...";
echo -e "\n\n-- The web application can be reached at localhost:8000  or  127.0.0.1:8000\n\n"

source .venv/bin/activate;		# Activate the virtual environment
python serverapp/manage.py runserver;	# Start the Django application on localhost
