import socket
from Crypto.Random import random
from Key_Generation import key_generation

S = socket.socket()
port = 12345
S.connect(('127.0.0.1', port))
print("Connected to Server")

S.recv(1024).decode()

n, e, s, v = key_generation()

rounds = random.randint(5, 10)
p_v = (n, e, v, rounds)

with open("public", "w") as f:
    f.write(" ".join(tuple(map(str, p_v))))

S.send("File created to access Public values".encode())
f = 0

for i in range(rounds):

    r = random.randint(1, 1000)
    x = pow(r, e, n)

    S.send(str(x).encode("utf-8"))

    msg = S.recv(1024).decode()
    c = int(msg)

    temp = pow(s, c)

    y = (temp * r) % n
    S.send(str(y).encode("utf-8"))

    reply = S.recv(1024).decode()

    if reply == "Pass":
        print(f"Passed {i + 1}'th successfully")

    else:
        print(f"Failed authentication at test {i + 1}")
        f = 1
        break

if f == 0:
    print("Verification done successfully")

S.close()
