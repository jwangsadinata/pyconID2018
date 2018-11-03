#!/usr/bin/env python3

from __future__ import print_function

import grpc

import pokemon_pb2
import pokemon_pb2_grpc

POKEMON_ID =  # TODO: fill this in


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = pokemon_pb2_grpc.PokemonServiceStub(channel)
        response = stub.Get(pokemon_pb2.GetReq(id=POKEMON_ID))
    print("Client received: Pokemon #%d is %s" % (response.id, response.name))


if __name__ == '__main__':
    run()
