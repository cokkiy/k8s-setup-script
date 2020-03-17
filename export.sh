#!/bin/sh
cd /var/lib/snapd/snap/microk8s/1247/actions
find ./ -type f | xargs grep image: >~/allimages.txt
