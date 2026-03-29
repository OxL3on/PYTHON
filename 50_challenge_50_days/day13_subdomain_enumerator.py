# Day 13: Subdomain Enumerator
# Read subdomains from a file, resolve each to an IP, print successes.
# Concepts: DNS resolution.

import socket

def check_subdomain(dns):
    subdomains = []
    try:
        with open("subdomains.txt", 'r') as file:
            for line in file:
                subdomains.append(f"{line.strip()}.{dns}")

    except FileNotFoundError:
        print("File Not Found")

    return subdomains


def main():
    dns = input("Enter Domain Name: ")
    
    subdomains = check_subdomain(dns)

    for i in subdomains:
        try:
            get_ip = socket.gethostbyname(i)
            print(f"{i} = {get_ip}")
        except socket.gaierror:
            continue
        except socket.error:
            continue
        except KeyboardInterrupt:
            print("KeyBoard Interrups...........CLOSING")
        
if __name__ == "__main__":
    main()