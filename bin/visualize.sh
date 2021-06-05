#!/usr/bin/bash

function run () {

tensorboard --logdir ./logs/

}

cd ..

source venv/bin/activate

run

deactivate

exit
