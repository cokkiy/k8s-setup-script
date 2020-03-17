#!/bin/sh
while read -r line ; do
            tar="./"$line    
            echo $tar        
            microk8s.ctr --namespace k8s.io image import $tar
            echo "${line} imported."
done