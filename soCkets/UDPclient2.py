import socket

def Main():
    host = '127.0.0.1'
    port = 5012

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    message = input('-> ')
    while message != 'quit':
        s.sendto(message.encode('utf-8'), (host, port))
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('recived from server', data)
        message = input('-> ')
    s.close()

Main()
