import socket
from utils import ConvertToBinary, GenerateKey, xor, ConvertToString

def Encyrpt(Message):
    # make sure message is divisible
    if len(Message) % 2 != 0:
        Message = Message + '-'

    cuttingPoint = int(len(Message) / 2)

    # splitting into two parts
    Left = Message[0:cuttingPoint]
    Right = Message[cuttingPoint:len(Message)]

    # convert ascii to binary for xor function
    Left = ConvertToBinary(Left)
    Right = ConvertToBinary(Right)

    # generate two keys
    KEY1 = GenerateKey(len(Left))
    KEY2 = GenerateKey(len(Right))

    # first stage
    L2 = Right
    R2 = xor(Left, xor(Right, KEY1))

    # second stage
    L3 = R2
    R3 = xor(L2, xor(R2, KEY2))

    # final reverese
    L4 = R3
    R4 = L3

    return L4 + R4, KEY1, KEY2


s = socket.socket()

print("socket created")

port = 12345

s.bind(('', port))
print(f'socket binded to port {port}')

s.listen(5)
print("Socket is listening")

while True:
    c, addr = s.accept()
    print(f'Connected to {addr}')

    Message = 'Hello There'

    Result, KEY1, KEY2 = Encyrpt(Message)

    keys = (KEY1, KEY2)
    with open("keys", "w") as f:
        f.write(" ".join(tuple(map(str, keys))))

    c.send(Result.encode())
    print("Encrypted msg: ",ConvertToString(Result))

    c.close()
    break
