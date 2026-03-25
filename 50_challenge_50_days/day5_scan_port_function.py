# Day 5: Functions (Reusable Scanner)
# Create a function scan_port(ip, port) that prints “Scanning [port]”.
# Concepts: function definition, parameters, return values.

def scan_port(ip, port):
    print(f"Scanning {ip}:{port}")

def main():
    ip = input("Enter IP: ")
    port = input("Enter PORT: ")
    scan_port(ip, port)

if __name__ == "__main__":
    main()