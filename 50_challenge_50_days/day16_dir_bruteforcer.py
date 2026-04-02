# Day 16: Directory Brute‑Forcer (Basic)
# Given a URL and a wordlist, try each path and report 200/403/404.
# Concepts: string concatenation, requests, filtering.

import requests


def main():
    url = input("Enter URL: ")
    try:
        with open("dir.txt", "r") as f:
            for line in f:
                try:
                    response = requests.get(url + "/" + line.strip())
                    if (
                        response.status_code == 200
                        or response.status_code == 404
                        or response.status_code == 401
                        or response.status_code == 403
                    ):
                        print(f"Url {url}/{line.strip()} = {response.status_code} ")
                except KeyboardInterrupt:
                    print("Keyboard Interrupt")
                    break
    except FileNotFoundError:
        print("File Not Found")


if __name__ == "__main__":
    main()
