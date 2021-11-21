import socket
from utils import xor, ConvertToString

def Decrypt(Message, KEY1, KEY2):
    cuttingPoint = int(len(Message) / 2)

    # splitting into two parts
    Left = Message[0:cuttingPoint]
    Right = Message[cuttingPoint:len(Message)]

    # first stage
    L2 = Right
    R2 = xor(Left, xor(Right, KEY1))

    # second stage
    L3 = R2
    R3 = xor(L2, xor(R2, KEY2))

    # final reverese
    L4 = R3
    R4 = L3

    return L4 + R4


s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))

res = s.recv(1024).decode()
print("Received msg: ", ConvertToString(res))

with open("keys", "r") as f:
    for line in f:
        KEY1, KEY2 = line.split(' ')


msg_dec = Decrypt(res, KEY2, KEY1)
print("Decrypted Message is: ", ConvertToString(msg_dec))
s.close()
