#!/bin/bash

# This script installs all necessary programs and tools to run the Django application
echo "Installing virtualenv"
sudo apt-get install virtualenv;

echo "Installing pip"
sudo apt-get install python-pip python-dev build-essential 
sudo pip install --upgrade pip 
sudo pip install --upgrade virtualenv 

source .venv/bin/activate;
echo "Installing django"
sudo pip install django;
