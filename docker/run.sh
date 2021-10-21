#!/bin/bash
# Create a docker image
docker build -t image_labs .

# Remove container container_42api
docker rm container_labs

# Run docker
docker run --name container_labs -it image_labs
