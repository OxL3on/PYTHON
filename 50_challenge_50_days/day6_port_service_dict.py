# Day 6: Lists & Dictionaries (Service Database)
# Store common ports and services in a dictionary (e.g., {22: "SSH", 80: "HTTP"}). Loop through and print them.
# Concepts: lists, dicts, iteration.


def main():
    ports_n_services = {
        21 : "FTP",
        22 : "SSH",
        80 : "HTTP",
        139 : "SMB",
        443 : "HTTPS"
    }

    for key, value in ports_n_services.items():
        print(f"Port {key} : Service {value}")

if __name__ == "__main__":
    main()