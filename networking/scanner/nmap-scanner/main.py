import subprocess


def network_scanner(host: str):
    res = subprocess.run(
        ["nmap", "-sV", "-p", "31000-32000", host],
        capture_output=True,
        text=True
    )

    open_ports = []

    for line in res.stdout.splitlines():
        if "open" in line:
            open_ports.append(line)

    return open_ports


def main():
    open_ports = network_scanner("localhost")

    for port in open_ports:
        print(port)


if __name__ == "__main__":
    main()
