#! /bin/bash

## install pip tool if not installed
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py

## create a environment
python3 -m venv env
source env/bin/activate

sleep 4

## Install the packages
pip install -r requirements.txt

sleep 4

## Execute the code
python3 download_OCO2_data_with_pydap.py
