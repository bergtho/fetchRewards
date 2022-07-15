#!/bin/bash

# Simple script to start the docker container

# I use a name for the container, so there can't be any containers already using it
# documentation: https://docs.docker.com/engine/reference/commandline/ps/
if [ $(docker ps -q -a --filter "ancestor=bergtho/fetchrewards"  --filter "name=fetch-rewards" ) ]; then
    echo "Please remove the container(s) with the following IDs before running this script: "
    echo $(docker ps -q -a --filter "ancestor=bergtho/fetchrewards"  --filter "name=fetch-rewards")
    exit 1
fi

docker build -t bergtho/fetchrewards .

# use 5000, also run in detached mode for curls from same terminal
docker run -p 5000:5000 -d --name fetch-rewards bergtho/fetchrewards

