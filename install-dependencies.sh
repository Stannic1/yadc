#!/bin/bash

# This script installs all necessary programs and tools to run the Django application
echo "Installing virtualenv"
sudo apt-get install virtualenv;

echo "Installing pip"
sudo apt-get install python-pip python-dev build-essential 
sudo pip3 install --upgrade pip 
sudo pip3 install --upgrade virtualenv 

source .venv/bin/activate;
echo "Installing django"
sudo pip3 install django;
sudo pip3 install docker
sudo pip3 install requests
