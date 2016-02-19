import socket
import sys
from _thread import *

host = "195.196.201.102"
port = 7777

clients = []
s.socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5)
print("Waiting for connection...")

def client(conn):
    conn.send(str.encode("> "))

    while True:
        data = conn.recv(2048)
