#!/bin/bash

# Check if virtual environment exists, if not create it
if [ ! -d "venv" ]
then
    python3 -m venv venv
fi

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirement/requirements-dev.txt

# Check if .flaskenv exists, if not create it
if [ ! -f ".flaskenv" ]
then
    echo "FLASK_ENV=$1" > .flaskenv
fi

# Deactivate virtual environment
deactivate
