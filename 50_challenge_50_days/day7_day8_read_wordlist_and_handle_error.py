# Day 7: File Handling (Reading Wordlists)
# Read a file with 10 common subdomains and print each.
# Concepts: open(), readlines(), handling file not found.

# Day 8: Exception Handling (Safe Scanner)
# Wrap the file reading in a try/except to catch missing files.
# Concepts: try/except, basic error handling.



def main():
    print_line = 10
    i = 0
    try: 
        with open("wordlist.txt") as file:
            for line in file:
                i += 1
                print(line.strip())
                if i == print_line:
                    break

    except (FileNotFoundError):
        print("File Not Found")

if __name__ == "__main__":
    main()