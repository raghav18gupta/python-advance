import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

server = 'https://pythonprogramming.net/'
port = 80

server_ip = socket.gethostbyname(server)
print(server_ip)

request = "GET / HTTP1.1\nHost: " + server +"\n\n"

s.connct((server, port))
s.send(request.encode())
result = s.recv(1024)
print(result)
