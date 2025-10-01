#!/bin/bash

logicModeSwitch="$1"
venv_path="$2"

if [ $logicModeSwitch = "-c" ]; then
    echo "Creating virtual environment at $venv_path"
    python3 -m venv $venv_path
elif [ $logicModeSwitch = "-r" ]; then
    echo "Activating virtual environment at $venv_path"
    source ${venv_path}/bin/activate
fi