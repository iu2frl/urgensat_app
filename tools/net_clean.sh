#!/bin/bash
sudo kill -9 `sudo lsof -t -i:5001`
sudo kill -9 `sudo lsof -t -i:5002`
sudo kill -9 `sudo lsof -t -i:1238`
sudo kill -9 `sudo lsof -t -i:1239`
