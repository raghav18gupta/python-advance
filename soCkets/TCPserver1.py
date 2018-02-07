import socket


def Main():
    host = '127.0.0.1'  #loopback address
    port = 5001

    s = socket.socket()     #TCP socket object
    s.bind((host, port))

    s.listen(1)     #one connection at a time
    c, addr = s.accept()
    print(str(addr) + " conneted ")
    while True:
        data = c.recv(1024).decode('utf-8')
        if not data:
            break
        print('client send: ' + data)
        data = data.upper()
        print('sending to client: ' + data)
        c.send(data.encode('utf-8'))
    c.close()
    print(str(addr) + ' connection closed')

Main()
#
# if __name__ = '__main__':
#     Main()







'''
bind()  #binds socket with port, used for tcp server
listen()    #instruct socket tostart listening for incoming TCP connection
accept()    #accept a connection when found, return new socket
recv()  #for both client and server'''
