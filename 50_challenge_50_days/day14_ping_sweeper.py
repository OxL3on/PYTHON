# Day 14: Ping Sweeper
# Ping a range of IPs using subprocess or ping command. Report alive hosts.
# Concepts: subprocess.run(), parsing output.

import subprocess
import socket


def is_alive(ip):
    result = subprocess.run(
        ["ping", "-c", "1", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )
    return result.returncode == 0

def main():
    subs = input("Enter subdomains: ").split()
    subs_to_ip = []
    for sub in subs:
        try:
            ip = socket.gethostbyname(sub)
            subs_to_ip.append(ip)
        except:
            continue

    for i in subs_to_ip:
        if is_alive(i):
            print(f"[+] {i} is alive")
        else:
            print(f"[-] {i} is not reachable")


if __name__ == "__main__":
    main()