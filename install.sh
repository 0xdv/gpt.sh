#!/bin/bash

set -eu

if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
  is_windows=true
else
  is_windows=false
fi

echo 'Clean up'
rm -rf venv-gpt

echo 'Create venv...'
if $is_windows; then
    python -m venv venv-gpt
else
    python3 -m venv venv-gpt
fi

echo 'Activate venv...'
if $is_windows; then
    source ./venv-gpt/Scripts/activate
else
    source ./venv-gpt/bin/activate
fi

echo 'Install requirements...'
pip install -r requirements.txt

echo ""
echo "Please reopen terminal or execute:"
if $is_windows; then
    echo "source ./venv-gpt/bin/activate"
else
    echo "source ./venv-gpt/bin/activate"
fi
