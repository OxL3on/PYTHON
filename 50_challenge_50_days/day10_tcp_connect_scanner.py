# Day 10: Simple TCP Connect Scanner
# Combine previous days: loop through a range of ports and attempt a TCP connection. Print open ports.
# Concepts: socket.connect_ex(), timeout, error handling.

import socket

def is_open(ip, port):
    try:
        tcp_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tcp_soc.settimeout(1)
        result = tcp_soc.connect_ex((ip, port))
        tcp_soc.close()
        return result == 0
    except socket.error:
        return False
    
def main():
    ip = input("Enter IP: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter End port: "))

    for i in range(start_port, end_port+1):
        if is_open(ip, i):
            print(f"Port {i} is Open")
        else:
            print(f"Scanning port {i} - CLOSED")
        

if __name__ == "__main__":
    main()