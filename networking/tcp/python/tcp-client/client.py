import socket


HOST = '127.0.0.1'
PORT = 30001



with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))
    while True:

        user_input = str(input('Wpisz słowo (exit = wyjscie):'))

        if user_input == 'exit':
            break

        s.sendall(user_input.encode("utf-8"))

        data = s.recv(1024)
        print('Received:', repr(data.decode("utf-8")))





    # s.connect((HOST, PORT))
    # s.sendall(b'test')
    # data = s.recv(1024)
