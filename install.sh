#!/bin/bash

set -eu

echo 'Clean up'
rm -rf venv-gpt

echo 'Create venv...'
python3 -m venv venv-gpt

echo 'Activate venv...'
source ./venv-gpt/bin/activate

echo 'Install requirements...'
pip install -r requirements.txt

echo ""
echo "Please reopen terminal or execute:"
echo "source ./venv-gpt/bin/activate"




