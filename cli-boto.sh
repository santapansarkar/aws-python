#!/bin/bash

source ./aws-venv-mac/bin/activate
python3 lab-first-boto.py --registryId $1 --repositoryName $2
