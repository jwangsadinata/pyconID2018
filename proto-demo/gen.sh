#!/bin/bash

set -ex

for lang in python go java ruby cpp csharp js php swagger; do
    mkdir -p $lang
    protoc -I=. --${lang}_out=./$lang pokemon.proto
done
