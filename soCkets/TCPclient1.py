import socket

def Main():
    host = '127.0.0.1'
    port = 5001

    s = socket.socket()
    s.connect((host, port))

    message = input('-> ')
    while message != 'quit':
        s.send(message.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')
        print('server send:   ' + data)
        message = input('->  ')
    s.close()

Main()








'''
connect()   #request connect to a listening server
recv()  #for both client and server
send()  #bytes to be send, eithr with byte() or encode() decode()
close() #close connection'''
