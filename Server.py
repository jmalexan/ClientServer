import socket

sock = socket.socket()
host = socket.gethostname()
port = 1337
sock.bind((host, port))

sock.listen(5)
while True:
    c, addr = sock.accept()
    print 'got connection from', addr
    c.send('Thank you for connecting')
    c.close()
