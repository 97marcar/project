import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "pythonprogramming.net"

def pscan(port):
    try:
        s.connect((server,port))
        return True
    except:
        return False

for n in range (1,26):
    if pscan(n):
        print("Port ",n," is open!!!!")
    else:
        print("Port ",n," is closed")
