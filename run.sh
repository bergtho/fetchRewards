#!/bin/bash

# This is just a script to start the docker container
# TODO: make the comments sound better

# using a name, so there can't be any containers already using it
# documentation: https://docs.docker.com/engine/reference/commandline/ps/
if [ $(docker ps -q -a --filter "ancestor=bergtho/fetchrewards"  --filter "name=fetch-rewards" ) ]; then
    echo "Please remove the container(s) with the following IDs before running this script: "
    echo $(docker ps -q -a --filter "ancestor=bergtho/fetchrewards"  --filter "name=fetch-rewards")
    exit 1
fi

# TODO: maybe make sure user is in the right directory

# TODO: instead of doing this, change the docker file and move it into this directory
cd flask_app

docker build -t bergtho/fetchrewards .

#docker run --rm -it --name fetch-rewards -p 5000:5000 bergtho/fetchrewards bash
# trying -i and -d and removing --rm

docker run -i -p 5000:5000 -d --name fetch-rewards bergtho/fetchrewards
# TODO: explain what -i does

# go back to the main directory
cd ..
