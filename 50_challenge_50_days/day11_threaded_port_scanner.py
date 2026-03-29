import socket
from concurrent.futures import ThreadPoolExecutor
import time

MAX_WORK = 10

def generate_port_chunk(port_range):
    start, end = map(int, port_range.split("-"))
    total_ports = end - start + 1
    chunk_size = total_ports // MAX_WORK
    remainder = total_ports % MAX_WORK

    port_chunks = []
    for i in range(MAX_WORK):
        s = start + chunk_size * i
        e = s + chunk_size - 1
        if i == MAX_WORK - 1:
            e += remainder
        port_chunks.append([s, e])
    return port_chunks

def check_port(ip, port_chunk):
    start, end = port_chunk
    print(f"Scanning {ip} from {start} to {end}")
    for port in range(start, end + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as tcp_port:
                tcp_port.settimeout(1)
                result = tcp_port.connect_ex((ip, port))
                if result == 0:
                    print(f"PORT {port} is OPEN.")
        except socket.error:
            pass

def main():
    ip = input("Enter IP: ")
    port_range = input("Enter port range (e.g. 1-1000): ")

    chunks = generate_port_chunk(port_range)

    start_time = time.time()

    with ThreadPoolExecutor(max_workers=MAX_WORK) as executor:
        executor.map(check_port, [ip] * len(chunks), chunks)

    end_time = time.time()

    start, end = port_range.split("-")
    print(f"Scanned {int(end)-int(start)+1} ports in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()