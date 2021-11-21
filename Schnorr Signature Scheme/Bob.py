import socket
from Verification import verify

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))

M = s.recv(1024).decode()
print("msg received")

with open("public_k", "r") as f:
    for line in f:
        p, e1, e2 = line.split(' ')

p = int(p)
e1 = int(e1)
e2 = int(e2)

s1 = int(s.recv(1024).decode('utf-8'))
print("s1 received: ")

s.send("send s2".encode())      # just to gap between consecutive receives via socket

s2 = int(s.recv(1024).decode('utf-8'))
print("s2 received: ")


verify(s1, s2, e1, e2, M, p)
