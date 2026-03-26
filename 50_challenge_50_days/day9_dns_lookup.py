# Day 9: Modules & Imports (Using socket)
# Import socket and get the IP of google.com.
# Concepts: modules, socket.gethostbyname().

import socket

def main():
    get_domain = input("Write the domain name: ")
    get_ip = socket.gethostbyname(get_domain)
    print(f"IP for {get_domain} is {get_ip}")

if __name__ == "__main__":
    main()