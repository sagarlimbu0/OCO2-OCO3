#!/bin/bash
IMAGE=oco_lab

docker build -t $IMAGE .

# run the image to browser
docker run -p 8888:8888 $IMAGE
