# TCP Client

Simple interactive TCP client written in Python.

## Features

* TCP socket creation
* Server connection
* Sending user input
* Receiving server responses
* UTF-8 encoding
* Interactive communication
* Exit command

## Usage

Run:

```bash
python client.py
```

Client connects to:

```text
127.0.0.1:30001
```

Enter a message to send it to the server.

Type:

```text
exit
```

to close the connection.

## Example

```text
Wpisz słowo (exit = wyjscie): hello
Received: 'hello'

Wpisz słowo (exit = wyjscie): test
Received: 'test'

Wpisz słowo (exit = wyjscie): exit
```

## Testing

Start the TCP server first:

```bash
python server.py
```

Then start the client:

```bash
python client.py
```

The client sends the entered message to the TCP server and prints the response.
