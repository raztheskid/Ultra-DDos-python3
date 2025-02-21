import os
import time
import sys

# Clear the screen and run the logo and server scripts
os.system("clear")
os.system("python3 src/logo.py")
os.system("python3 src/serv.py")

# Define some colors for the terminal output
Green = "\033[1;33m"
Blue = "\033[1;34m"
Grey = "\033[1;30m"
Reset = "\033[0m"
Red = "\033[1;31m"
Purple = "\033[0;35m"

g = "\033[1;32m"
r = "\033[1;31m"
w = "\033[0m"
b = "\033[1;34m"
o = "\033[1;33m"
bl = "\033[1;36;40m"

# Print the menu options
print("1. DDos Ip Address")
print("2. View Url Ip Address")
print("3. DDos site logs")

# Get user input
try:
    op = int(input("Options: "))
    if op == 1:
        os.system("python3 src/ddos.py")
    elif op == 2:
        os.system("python3 src/Url.py")
    elif op == 3:
        os.system("python3 src/log-ddos.py")
    else:
        print(f"{r}Invalid input. Reloading Tools!{Reset}")
        time.sleep(1.6)
        os.system("cd")
        os.system("cd Ultra-DDos")
        os.system("python3 main.py")
except ValueError:
    print(f"{r}Invalid input. Enter a number, dumbass.{Reset}")
    time.sleep(1.6)
    os.system("python3 main.py")
