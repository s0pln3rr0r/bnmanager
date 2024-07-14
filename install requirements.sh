#!/bin/bash

# Function to check if a command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check if Python 3 is installed
if ! command_exists python3; then
    echo "Python 3 is not installed. Installing..."
    sudo apt update
    sudo apt install -y python3
    echo "Python 3 installed successfully."
else
    echo "Python 3 is already installed."
fi
    sudo apt install -y netcat

# Install required Python modules using pip3
echo "Installing required Python modules..."
sudo pip3 install --upgrade pip
sudo pip3 install os time sqlite3 termcolor
echo "Required Python modules installed successfully."
cp bnmanager.py /bin/bnmanager.py
