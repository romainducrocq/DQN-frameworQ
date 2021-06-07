#!/usr/bin/bash

function run () {

if [ "$1" = "-test" ]; then
  tensorboard --logdir ./logs/test/
else
  tensorboard --logdir ./logs/train/
fi

}

cd ..

source venv/bin/activate

run "$1"

deactivate

exit
