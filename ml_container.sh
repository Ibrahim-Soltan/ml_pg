#!/bin/bash

# Define variables
IMAGE_NAME="ml-playground-image"
CONTAINER_NAME="ml-playground-container"
LOCAL_DIR="$(pwd)"
WORK_DIR="/workspace"

# Build the Docker image
docker build -t $IMAGE_NAME .

# Run the Docker container with GPU support and bind mount
docker run --gpus all --name $CONTAINER_NAME -v $LOCAL_DIR:$WORK_DIR -it --rm $IMAGE_NAME
