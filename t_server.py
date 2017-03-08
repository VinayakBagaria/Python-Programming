import socket
"""
    socket.socket() creates a socket object
"""

s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
"""
    s.bind() - this method binds the address (hostname,port) to socket for knowing where to connect
"""
s.bind((host,port))
"""
    s.listen() sets up and starts TCP-IP listener
"""
s.listen()
while True:
    """
        this method passively accepts TCP-IP client connection, waiting until the connection arrives
    """
    c,addr=s.accept()
    print('Got Connection from ',addr)
    c.send(b'Connected')
    print(c.recv(1024))
    while True:
        c.send(str.encode(input()))
        print(c.recv(1024))
c.close()