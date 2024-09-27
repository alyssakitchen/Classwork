#!/usr/bin/env bash

externalIP=$1

eval "$(ssh-agent -s)"
ssh-add ~/.ssh/gcp
ssh -i gcp amkitchen42@$1