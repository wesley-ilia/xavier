#!/bin/bash


# Verify if containner exist
if docker ps -a --format '{{.Names}}' | grep -Eq "^container_sonar\$"; then
    docker restart container_sonar
else
    #Create a docker image
    docker build -t image_sonarqube .
    docker run --name container_sonar -p 9000:9000 -it image_sonarqube
fi

