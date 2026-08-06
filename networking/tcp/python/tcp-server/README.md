# TCP Server

Simple TCP echo server written in Python.

## Features

- TCP socket creation
- Client connection handling
- Timeout support
- Error handling

## Usage

Run:

python server.py

Server starts on:

127.0.0.1:30001

## Testing

Using netcat:

echo "hello" | ncat 127.0.0.1 30001
