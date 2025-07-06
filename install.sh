#!/bin/bash

if command -v ml &> /dev/null ; then
    echo "Loading modules."
    ml Python
    ml OpenMPI
fi

python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
