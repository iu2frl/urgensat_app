#!/bin/bash
sudo kill -9 `sudo lsof -t -i:5001`
sudo kill -9 `sudo lsof -t -i:5002`
sudo kill -9 `sudo lsof -t -i:1238`
sudo kill -9 `sudo lsof -t -i:1239`
pkill -9 -f app.py
pkill -9 -f app.py
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
cd $SCRIPT_DIR
clear
/usr/bin/python2 -u ./top_block.py
