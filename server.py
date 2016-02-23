import socket
import sys
from _thread import *

host = ""
port = 7777

clients = []
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5)
print("Waiting for connection...")


def client(conn):
    name = input("Enter Name: ")
    conn.send(str.encode("> "))

    while True:
        data = conn.recv(2048)
        reply = name +": "+ data.decode("utf-8")
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

while True:
    conn, addr = s.accept()
    print("connected to: "+addr[0]+":"+str(addr[1]))
    print("connected to: "+addr2[0]+":"+str(addr2[1]))

    start_new_thread(client(conn,), client(conn2,))
