#!/bin/bash
# Create a docker image
docker build -t image_thor1 .

# Remove container container_42api
#docker rm container_labs

# Run docker
docker run --name container_thor1 -it image_thor1
