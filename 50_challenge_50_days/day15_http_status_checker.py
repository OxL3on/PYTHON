# Day 15: HTTP Request with requests
# Install the requests module. Fetch a webpage and print the status code.
# Concepts: pip, requests.get(), status codes.

import requests


def main():
    url = input("Enter your Website URL: ")

    response = requests.get(url)
    print(response.text)
    print(response.status_code)


if __name__ == "__main__":
    main()
