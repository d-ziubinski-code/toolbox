import socket
import logging
import platform

HOST = '127.0.0.1'
PORT = 30001
uname = platform.uname()


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
            logging.StreamHandler()
        ]


)

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

    logging.info(f"Klient podłączony {addr}")

    with conn:
        while True:
            data = conn.recv(1024)

            if not data:
                logging.info(f"Klient {addr} rozłączył się.")
                break


            message = data.decode("utf-8")

            logging.debug(f"Odebrane bajty od {addr}: {data}")
            logging.info(f"Odebrana wiadomość od {addr}: {message.strip()}")


            response = f"Serwer {uname.machine} otrzymał wiadomość {message.strip()} "
            conn.sendall(response.encode("utf-8"))




if __name__ == "__main__":
    start_server(HOST, PORT)
