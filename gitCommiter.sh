#!/bin/bash

cMessage=$1

git add -A *.tex fig* gitCommiter.sh 
echo "Do you want to commit with message: "$cMessage"?"
echo "enter to continue - ctrl-c to skip"
read
git commit -m "$cMessage"
