# PyConID 2018

## What is it?

This repository contains the presentation slide and demo files for my
talk at PyCon Indonesia 2018, on **"Demystifying GRPC: The Modern Toolkit for
Microservices**.

## Trying the demo

There are two demos being presented at the talk, one on `protobuf` and another
on `grpc`. The demos are being put into separate directory `proto-demo` and
`grpc-demo`.

### proto-demo

This directory just contains the `.proto` file, and two scripts to help
generate the client libraries from the aforementioned file. To generate the
client libraries, you can do:

    $ ./gen.sh

You should be able to see the command being run interactively, then you can also
examine each of the generated artifacts.

To clean up, you can simply run:

    $ ./cleanup.sh

and it will remove all the generated artifacts.

### grpc-demo

Similarly, this directory contains the `.proto` file, a generator script and a
`python` directory where the `client` and `server` code is already predefined.
To generate the python client libraries and grpc stubs, you can also run:

    $ ./gen.sh

It will generate the `${FILENAME}_pb2.py` and `${FILENAME}_pb2_grpc.py`, which
you can use to create the `client` and `server` program.

The `client.py` and `server.py` is incomplete, but I will leave it as an
exercise for the reader to try to finish it. The idea is for the client to be
able to get the Pokemon's `name` by just sending the `id`. There is a file
called `pokemon.py`, containing a simple dictionary for Pokemon names that you
can use.

To execute the program, you can do the following:

- First, start the server

      $ ./server.py

- Then, on a separate session (terminal window), start the client

      $ ./client.py

- Verify that the client received the appropriate response from the server.

## Acknowledgements

- [`gRPC`][grpc]
- [`Protocol Buffers`][protobuf]
- [`gRPC: From Tutorial to Production - Alan Shreve`][talk]

[grpc]: https://grpc.io
[protobuf]: https://grpc.io/docs/guides/#working-with-protocol-buffers
[talk]: https://www.youtube.com/watch?v=7FZ6ZyzGex0&t
