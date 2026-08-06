import socket

HOST = '127.0.0.1'
PORT = 30001



def start_server(host, port):

    try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:

                server.bind((host, port))
                server.listen(1)
                server.settimeout(1)
                print(f"Server listening on {host}:{port}")

                while True:
                    try:
                        conn, addr = server.accept()
                        handle_client(conn, addr)
                    except socket.timeout:
                        continue

    except KeyboardInterrupt:
        print("Server stopped...")

    except OSError as e:
        print(f"Socket Error: {e}")

    except Exception as e:
        print(f"Server error: {e}")



def handle_client(conn, addr):


    with conn:
        print('Connected by:', addr)

        while True:
            data = conn.recv(1024)

            if not data:
                break

            conn.sendall(data)




if __name__ == "__main__":
    start_server(HOST, PORT)
