#!/bin/bash

# Install required packages
sudo apt install python3 python3-pip python3-dev graphviz libgraphviz-dev pkg-config

# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install required Python packages
pip install -r requirements.txt
