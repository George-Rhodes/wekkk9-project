#!/bin/bash
sudo apt update
sudo apt install python3 python3-pip python3-venv -y
python3 -m venv venf 
. ./venf/bin/activate
pip3 install -r requirements.txt
cd service-2
pytest --cov ./application 
cd ..
cd service-3
pytest --cov ./application 
cd ..
cd service-4
pytest --cov ./application 
cd ..


deactivate

rm -rf venf