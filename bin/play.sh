#!/usr/bin/bash

cd ../

source venv/bin/activate
if [ -z "${1}" ]; then
    python3 play.py
else
    python3 play.py "${@}"
fi
deactivate

exit
