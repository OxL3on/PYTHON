

## Weeks 1–2: Python Fundamentals (Security Context)

**Day 1: Hello, World!**  
Write a script that prints “Hello, Hacker!”. Learn to run Python scripts.  
*Concepts:* print(), basic script execution.

**Day 2: Variables & User Input**  
Ask the user for their name and IP address, then print them.  
*Concepts:* variables, input(), type conversion.

**Day 3: Conditional Logic (Simple Banner Grabber)**  
Take a user’s choice (1 for HTTP, 2 for SSH) and print a banner.  
*Concepts:* if/elif/else, comparison operators.

**Day 4: Loops (Port Range Generator)**  
Use a for loop to print ports 1–1024. Then modify to ask user for a range.  
*Concepts:* for loops, range(), while loops.

**Day 5: Functions (Reusable Scanner)**  
Create a function `scan_port(ip, port)` that prints “Scanning [port]”.  
*Concepts:* function definition, parameters, return values.

**Day 6: Lists & Dictionaries (Service Database)**  
Store common ports and services in a dictionary (e.g., `{22: "SSH", 80: "HTTP"}`). Loop through and print them.  
*Concepts:* lists, dicts, iteration.

**Day 7: File Handling (Reading Wordlists)**  
Read a file with 10 common subdomains and print each.  
*Concepts:* open(), readlines(), handling file not found.

**Day 8: Exception Handling (Safe Scanner)**  
Wrap the file reading in a try/except to catch missing files.  
*Concepts:* try/except, basic error handling.

**Day 9: Modules & Imports (Using `socket`)**  
Import `socket` and get the IP of google.com.  
*Concepts:* modules, `socket.gethostbyname()`.

**Day 10: Simple TCP Connect Scanner**  
Combine previous days: loop through a range of ports and attempt a TCP connection. Print open ports.  
*Concepts:* `socket.connect_ex()`, timeout, error handling.

---

## Weeks 3–4: Networking & Basic Automation

**Day 11: Port Scanner with Threading**  
Make your port scanner faster using threading (limit to 10 threads at a time).  
*Concepts:* threading, queue.

**Day 12: Service Banner Grabber**  
After connecting to an open port, send a simple request and read the banner.  
*Concepts:* `socket.send()`, `recv()`, encoding.

**Day 13: Subdomain Enumerator**  
Read subdomains from a file, resolve each to an IP, print successes.  
*Concepts:* DNS resolution, threading again.

**Day 14: Ping Sweeper**  
Ping a range of IPs using `subprocess` or `ping` command. Report alive hosts.  
*Concepts:* `subprocess.run()`, parsing output.

**Day 15: HTTP Request with `requests`**  
Install the `requests` module. Fetch a webpage and print the status code.  
*Concepts:* pip, `requests.get()`, status codes.

**Day 16: Directory Brute‑Forcer (Basic)**  
Given a URL and a wordlist, try each path and report 200/403/404.  
*Concepts:* string concatenation, `requests`, filtering.

**Day 17: Web Crawler (Extract Links)**  
Crawl a single page, extract all `<a href>` links, and print them.  
*Concepts:* BeautifulSoup, regex or HTML parsing.

**Day 18: Simple Keylogger (Educational)**  
Log keystrokes to a file using `pynput` (run only in your lab).  
*Concepts:* event listener, logging.

**Day 19: Reverse Shell (Listener)**  
Write a simple listener that waits for a connection and executes commands.  
*Concepts:* sockets, `subprocess`, command loop.

**Day 20: Reverse Shell (Client)**  
Write a client that connects back and sends command output. Test on two VMs.  
*Concepts:* client/server architecture, encoding/decoding.

---

## Weeks 5–6: Web & Credential Attacks

**Day 21: Password Generator**  
Generate random passwords with specified length and complexity.  
*Concepts:* `random`, string modules.

**Day 22: Hash Cracker (Single Hash)**  
Given a MD5 hash, compare it against a list of words (dictionary attack).  
*Concepts:* hashlib, file reading, benchmarking.

**Day 23: Brute‑Force Login (HTTP Form)**  
Use `requests` to POST username/password combos to a login form.  
*Concepts:* POST data, session handling, timing.

**Day 24: SSH Brute‑Forcer with `paramiko`**  
Attempt to log into SSH using a password wordlist.  
*Concepts:* `paramiko`, threading, error handling.

**Day 25: SQL Injection Tester (Error‑Based)**  
Inject a single quote and check for SQL errors in the response.  
*Concepts:* payloads, response content analysis.

**Day 26: XSS Scanner (Reflected)**  
Insert a simple `<script>alert(1)</script>` and see if it’s echoed back.  
*Concepts:* payload encoding, response searching.

**Day 27: FTP Brute‑Forcer**  
Use `ftplib` to attempt logins on an FTP server.  
*Concepts:* `ftplib`, login exceptions.

**Day 28: Command Injection Tester**  
Append `; ls` to a parameter and check output for system command results.  
*Concepts:* parameter injection, output inspection.

**Day 29: Simple Web Shell**  
Create a PHP‑like shell that executes system commands via a web parameter.  
*Concepts:* CGI or Flask, `subprocess`.

**Day 30: Logging & Reporting**  
Take one of your scanners and make it write results to a CSV or JSON file.  
*Concepts:* CSV/JSON modules, structured output.

---

## Weeks 7–8: Post‑Exploitation & Advanced Automation

**Day 31: Persistence via Registry (Windows)**  
Add your Python script to Windows Registry run key (lab only).  
*Concepts:* `winreg`, administrative privileges.

**Day 32: Screenshot Capturer**  
Take a screenshot and save it using `PIL` or `pyautogui`.  
*Concepts:* image handling, scheduling.

**Day 33: Clipboard Monitor**  
Monitor clipboard changes and log them (educational).  
*Concepts:* `pyperclip`, loops.

**Day 34: File Encryptor/Decryptor**  
Write a script that XOR‑encrypts a file and then decrypts it.  
*Concepts:* byte operations, file I/O.

**Day 35: Packet Sniffer with `scapy`**  
Capture TCP packets and print source/destination.  
*Concepts:* `scapy`, packet layers.

**Day 36: ARP Spoofer (Proof of Concept)**  
Send ARP replies to poison the cache (lab only).  
*Concepts:* ARP protocol, `scapy`.

**Day 37: DNS Spoofing**  
Respond to DNS queries with fake IPs (lab only).  
*Concepts:* `scapy`, DNS layer.

**Day 38: Wi‑Fi Deauther (with Monitor Mode)**  
Send deauthentication packets to disconnect clients (lab only).  
*Concepts:* 802.11 frames, monitor mode.

**Day 39: C2 Basic (HTTP)**  
Create a simple C2 that uses HTTP requests to fetch commands and send results.  
*Concepts:* Flask server, `requests` client.

**Day 40: Telegram Bot for Alerts**  
Make a bot that sends a message when a new open port is found.  
*Concepts:* Telegram Bot API, asynchronous handling.

---

## Weeks 9–10: Final Projects & Integration

**Day 41: Vulnerability Scanner – Port + Service + Common CVE**  
Combine port scan, banner grab, and a CSV of known vulnerable versions.  
*Concepts:* data lookup, reporting.

**Day 42: Automated Recon**  
Write a script that runs subdomain enumeration, port scan, and screenshots automatically.  
*Concepts:* subprocess, modular code, logging.

**Day 43: Linux Privilege Escalation Checker**  
Check SUID files, sudo rights, cron jobs, and print findings.  
*Concepts:* `os`, `subprocess`, file permissions.

**Day 44: Windows Enumeration Script**  
Collect system info, users, services, and network config.  
*Concepts:* WMI, `win32api`, `subprocess`.

**Day 45: Phishing Simulator (Educational)**  
Create a fake login page with Flask that logs credentials (use in lab only).  
*Concepts:* Flask, POST data, session.

**Day 46: Maldoc Generator (Word with Macro)**  
Create a Word document that contains a malicious macro (simulated).  
*Concepts:* `docx` library, macro basics.

**Day 47: Command & Control with Encryption**  
Add AES encryption to your C2 communication.  
*Concepts:* cryptography, key exchange.

**Day 48: Full Pentest Report Generator**  
Take all scan outputs and create a formatted HTML report.  
*Concepts:* Jinja2, templating.

**Day 49: Metasploit Resource Script Generator**  
Generate `.rc` scripts for Metasploit to automate attacks.  
*Concepts:* file writing, Metasploit automation.

**Day 50: Build Your Own Toolkit**  
Create a menu‑driven script that combines your favorite tools from the past 49 days.  
*Concepts:* package structure, argparse, help menus.



<br>
<br>

day1_hello_hacker
day2_name_ip_input
day3_banner_chooser
day4_port_range_generator
day5_scan_port_function
day6_port_service_dict
day7_read_wordlist
day8_safe_file_reader
day9_dns_lookup
day10_tcp_connect_scanner
day11_threaded_port_scanner
day12_banner_grabber
day13_subdomain_enumerator
day14_ping_sweeper
day15_http_status_checker
day16_dir_bruteforcer
day17_link_extractor
day18_keylogger
day19_reverse_shell_listener
day20_reverse_shell_client
day21_password_generator
day22_hash_cracker
day23_http_bruteforcer
day24_ssh_bruteforcer
day25_sqli_tester
day26_xss_scanner
day27_ftp_bruteforcer
day28_cmd_injection_tester
day29_web_shell
day30_json_csv_reporter
day31_registry_persistence
day32_screenshot_capture
day33_clipboard_monitor
day34_xor_file_encryptor
day35_packet_sniffer
day36_arp_spoofer
day37_dns_spoofer
day38_wifi_deauther
day39_http_c2
day40_telegram_bot
day41_vuln_scanner
day42_automated_recon
day43_linux_privesc_checker
day44_windows_enum
day45_phishing_simulator
day46_maldoc_generator
day47_encrypted_c2
day48_report_generator
day49_metasploit_rc_generator
day50_toolkit
