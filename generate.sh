#!/bin/bash

rm -rf _library/*
for module in $(shpc show); do          
    flatname=${module#/}
    name=$(echo ${flatname//\//-})
    echo "Generating docs for $module, _library/$name.md"
    shpc docgen --registry https://github.com/singularityhub/shpc-registry $module > "_library/${name}.md"
done
