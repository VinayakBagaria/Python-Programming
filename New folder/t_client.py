import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=12345
"""
    This method here initiates TCP server connection
"""
s.connect((host,port))
print(s.recv(1024))
s.send(b'From client')


while True:
    print(s.recv(1024))
    s.send(str.encode(input()))
s.close()

"""
    s.recv() - receive message
    s.send() - transmit messsage
    
"""