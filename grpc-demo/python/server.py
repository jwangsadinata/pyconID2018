#!/usr/bin/env python3

from concurrent import futures
import time

import grpc

import pokemon_pb2
import pokemon_pb2_grpc


class PokemonService(pokemon_pb2_grpc.PokemonServiceServicer):

    def Get(self, request, context):
        # TODO: write the server logic here
        return pokemon_pb2.Pokemon()


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pokemon_pb2_grpc.add_PokemonServiceServicer_to_server(
            PokemonService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    serve()
