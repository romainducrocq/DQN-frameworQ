#!/usr/bin/bash

cd ../

# Get dependencies

sudo apt-get update
sudo apt-get install build-essential libpq-dev libssl-dev openssl libffi-dev \
    sqlite3 libsqlite3-dev libbz2-dev zlib1g-dev g++ cmake

# Install Python 3.7.12 locally

if [ -f "Python-3.7.12.tar.xz" ]; then rm -v Python-3.7.12.tar.xz; fi
if [ -d "Python-3.7.12" ]; then rm -rv Python-3.7.12/; fi
wget https://www.python.org/ftp/python/3.7.12/Python-3.7.12.tar.xz
tar xvf Python-3.7.12.tar.xz
cd Python-3.7.12/
./configure
make
cd ../
rm -rv Python-3.7.12.tar.xz

# Make venv and install pip3 packages

if [ -d "venv" ]; then rm -rv venv/; fi
mkdir -v venv/
Python-3.7.12/python -m venv venv/
source venv/bin/activate
export TMPDIR='/var/tmp'
pip3 install six numpy 'pyglet==1.5.0' gym torch tensorboard 'msgpack==1.0.2' \
    wheel --no-cache-dir
deactivate

exit