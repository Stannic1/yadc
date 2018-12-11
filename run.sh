#!/bin/bash

# This run script handles starting the localhost server for the Django project.
echo "Starting the Django web application on localhost...";

source .venv/bin/activate;		# Activate the virtual environment
python serverapp/manage.py runserver;	# Start the Django application on localhost
