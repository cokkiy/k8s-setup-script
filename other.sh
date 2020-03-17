#! /bin/sh

docker pull $1
docker save $1 > $2