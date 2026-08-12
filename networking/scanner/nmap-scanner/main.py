import logging
import subprocess
import sys
import ssl
import socket

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    handlers=[
            logging.StreamHandler()
        ]


)

def network_scanner(host: str, ports: str):
    res = subprocess.run(
        ["nmap", "-sV", "-p", ports, host],
        capture_output=True,
        text=True
    )

    open_ports = []

    for line in res.stdout.splitlines():
        if "open" in line:
            open_ports.append(line)

    return open_ports


def ssl_connection(host: str, port: int, password: str):
    context = ssl.create_default_context()
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE


    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        with context.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.connect((host, port))
            ssock.sendall(f"{password}\n".encode("utf-8"))

            response = ssock.recv(4096)
            return response.decode("utf-8", errors="ignore")




def main(host, ports):

    with open("/etc/bandit_pass/bandit16", 'r') as f:
        password = f.read().strip()

    open_ports = network_scanner(host, ports)


    for port in open_ports:
        raw_port, status, tech = port.split(maxsplit=2)

        if 'ssl' in tech:
            port_num = int(raw_port.split("/")[0])
            logging.info(f"\n [+] Próba połączenia z {tech} na porcie {port_num}")

            try:
                resp = ssl_connection(host, port_num, password)
                logging.info(f"Odpowiedz z portu {port_num}:\n{resp}")
            except Exception as e:
                logging.info(f"Błąd na porcie {num_port}: {e}")



if __name__ == "__main__":
    if len(sys.argv) < 3:
        logging.info("Użycie: python skrypt.py <host> <porty>")
        logging.info("Przykład: python main.py 127.0.0.1 31000-32000 ")
        sys.exit(1)

    host = sys.argv[1]
    ports = sys.argv[2]
    main(host, ports)
