#! /bin/sh

docker pull $1
docker tag $1 $2
docker save $2 > $3