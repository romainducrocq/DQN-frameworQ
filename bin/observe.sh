#!/usr/bin/bash

cd ../

source venv/bin/activate
if [ -z "${1}" ]; then
    python3 observe.py -d save/DuelingDoubleDQNAgent_lr0.0001_model.pack
else
    python3 observe.py "${@}"
fi
deactivate

exit
