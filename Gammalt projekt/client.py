import socket
import threading
import time

tLock = threading.Lock()
shutdown = False

def receving(name, sock):
    while not shutdown:
        try:
            tLock.acquire()
            while True:
                data, addr = sock.recvfrom(1024)
                str4print = data.decode("utf-8")
                print(str4print)
        except:
            pass

        finally:
            tLock.release()

host = "192.168.45.61"
port = 0

server = ("192.168.45.61", 8989)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind((host, port))

s.setblocking(0)

rT = threading.Thread(target=receving, args=("RecvThread", s))
rT.start()

alias = input("Name: ")
message = input(alias + "->")

while message != "q":
    if message != "":
        string = (alias + ': ' + message)
        byte = string.encode("utf-8")
        s.sendto(byte, server)

    tLock.acquire()
    message = input(alias + "-->")
    tLock.release()


shutdown = True

rT.join()
s.close()
