import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "pythonprogramming.net"
port = 80

server_ip = socket.gethostbyname(server) #tar ip
print(server_ip)


request = "Get / HTTP/1.1\nHost: "+server+"\n\n"

s.connect((server,port))
s.send(request.encode())
result = s.recv(4096)

#print(result) #printar allt som hämtats ned recv

#buffering in action
while (len(result) > 0):
    print(result)
    result = s.recv(4096)
