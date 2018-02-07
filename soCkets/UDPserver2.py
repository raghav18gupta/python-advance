import socket

def Main():
    host = '127.0.0.1'
    port = 5012

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))

    print('server started')
    while True:
        data, addr = s.recvfrom(1024)
        data = data.decode('utf-8')
        print('message from client' + str(addr) + " : " + str(data))
        data = data.upper()
        print('sending to client : ', str(data))
        s.sendto(data.encode('utf-8'), addr)
    s.close()


Main()



'''
same programm, but with unreliable fast UDP
here we use recvfrom() and sendto()
'''
