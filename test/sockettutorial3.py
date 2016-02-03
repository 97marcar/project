import threading
import socket
from queue import Queue

print_lock = threading.Lock()

target = "facebook.com"

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print("port ",port," is open")

        con.close()

    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()
q = Queue()

for n in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,10000):
    q.put(worker)
q.join()
