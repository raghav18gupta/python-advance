import socket

def Main():
    host = '127.0.0.1'
    port = 7468
    server = (host, 7400)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input('-> ')
    while message != 'quit':
        s.sendto(message.encode('utf-8'), server)
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('recived from server', data)
        message = input('-> ')
    s.close()

Main()
