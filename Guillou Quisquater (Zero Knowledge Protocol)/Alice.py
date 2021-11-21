import socket
from Crypto.Random import random

s = socket.socket()

print("socket created")

port = 12345

s.bind(('', port))
print(f'socket binded to port {port}')

s.listen(1)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print(f'Connected to {addr}')

    # send a thank you message to the client.
    c.send('Thank you for connecting'.encode())

    conf = c.recv(1024).decode()
    print(conf)

    with open("public", "r") as f:
        for line in f:
            n, e, v, rounds = line.split(' ')

    n = int(n)
    e = int(e)
    v = int(v)
    rounds = int(rounds)

    f = 0

    for i in range(rounds):

        x = c.recv(1024).decode()
        x = int(x) % n

        chal = random.randint(1, 1000)

        c.send(str(chal).encode())

        y = int(c.recv(1024).decode())

        res = (pow(y, e, n) * pow(v, chal, n)) % n

        if res == x:
            print(f"Pass {i + 1}th test")
            c.send("Pass".encode("utf-8"))
        else:
            print(f"Failed {i+1}th test ")
            c.send("Fail".encode("utf-8"))

    c.close()
    break
