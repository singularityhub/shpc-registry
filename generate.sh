#!/bin/bash

registry="${1}"
printf "Registry is ${registry}"

rm -rf _library/*
for module in $(shpc show --registry ${registry} ); do          
    flatname=${module#/}
    name=$(echo ${flatname//\//-})
    echo "Generating docs for $module, _library/$name.md"
    shpc docgen --registry ${registry} --registry-url https://github.com/singularityhub/shpc-registry $module > "_library/${name}.md"
done
