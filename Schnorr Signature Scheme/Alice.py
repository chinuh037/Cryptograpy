import socket
from Key_Generation import generate_keys
from Signing import signing

s = socket.socket()

print("socket created")

port = 12345

s.bind(('', port))
print(f'socket binded to port {port}')

s.listen(5)
print("Socket is listening")

M = "Hello"

public, d = generate_keys()
(p, e1, e2) = public

with open("public_k", "w") as f:
    f.write(" ".join(tuple(map(str,public))))

while True:
    c, addr = s.accept()
    print(f'Connected to {addr}')

    s1, s2 = signing(e1, M, p, d)

    # send M
    c.send(M.encode())
    print("Msg sent")

    c.send(str(s1).encode('utf-8'))
    print(f"s1 sent")

    c.recv(1024).decode()   # just to gap between consecutive sends

    c.send(str(s2).encode('utf-8'))
    print(f"s2 sent")

    c.close()
    break
