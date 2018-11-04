#!/bin/bash

set -ex

for lang in python go java ruby cpp csharp js php swagger; do
    if [ -d $lang ]; then
        rm -rf $lang
    fi
done
