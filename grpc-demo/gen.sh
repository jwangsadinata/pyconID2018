#!/bin/bash

set -ex

python3 -m grpc_tools.protoc -I=. --python_out=./python --grpc_python_out=./python pokemon.proto
