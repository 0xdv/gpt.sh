#!/bin/bash

set -euv

echo 'Clean up'
rm -rf venv-gpt

echo 'Create venv...'
python3 -m venv venv-gpt

echo 'Activate venv...'
source ./venv-gpt/bin/activate

echo 'Install requirements...'
pip install -r requirements.txt




