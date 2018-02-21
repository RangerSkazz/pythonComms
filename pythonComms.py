import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = 172.0.0.1
port = 1002
s.connect((ip ,port ))

date = s.recv(512)
print date