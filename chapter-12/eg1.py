#Retrieving text over HTTP
import socket

mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST='data.pr4e.org'
PORT=80
mysock.connect((HOST,PORT))
cmd='GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data=mysock.recv(1024)
    if len(data)<1:
        break
    print(data.decode(),end=' ')
mysock.close()