#!/bin/bash

# This script installs all necessary programs and tools to run the Django application
echo "Installing pip"
sudo apt-get install python3-pip python3-dev build-essential 
sudo pip3 install --upgrade pip 
sudo pip3 install --upgrade virtualenv 

echo "Installing django"
sudo pip3 install django;
sudo pip3 install docker
sudo pip3 install requests
