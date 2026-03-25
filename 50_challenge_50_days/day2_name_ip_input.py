# Day 2: Variables & User Input
# Ask the user for their name and IP address, then print them.
# Concepts: variables, input(), type conversion.

def main():
    get_name = input("What is your name? : ")
    get_ip_addr = input("What is your IP Address? : ")

    print(f"{get_name} {get_ip_addr}")

if __name__ == "__main__":
    main()