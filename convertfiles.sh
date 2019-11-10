#!/usr/bin/env bash

cd $1
for d in *; do
    r="$(echo $d | egrep -o '(.+)(\.)')png"
    convert $d ../corpus/$r
done
