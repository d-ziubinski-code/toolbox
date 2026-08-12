import logging
import subprocess
import sys


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


def main(host, ports):
    open_ports = network_scanner(host, ports)

    for port in open_ports:
        print(port)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        logging.info("Użycie: python skrypt.py <host> <porty>")
        logging.info("Przykład: python main.py 127.0.0.1 31000-32000 ")
        sys.exit(1)

    host = sys.argv[1]
    ports = sys.argv[2]
    main(host, ports)
