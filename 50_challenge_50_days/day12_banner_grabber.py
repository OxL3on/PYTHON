# Day 12: Service Banner Grabber
# After connecting to an open port, send a simple request and read the banner.
# Concepts: socket.send(), recv(), encoding.

import socket

def grab_banner(ip, port):
    try:
        s = socket.socket()

        s.settimeout(1)

        s.connect((ip, port))
        s.send(f"GET / HTTP/1.1\r\nHost: {ip}\r\n\r\n".encode())
        print(s.recv(1024).decode())

        s.close()
    except Exception as e:
        print(f"Error: {e}")


def main():
    ip = input("Enter IP Address/DNS: ")
    port = int(input("Enter port number: "))
    grab_banner(ip, port)

if __name__ == "__main__":
    main()