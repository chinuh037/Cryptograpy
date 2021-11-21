import socket
from utils import getLength, byte_xor, get_padded_msg
from Crypto.Cipher import DES

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

    # 64 bit key
    key = b'I_am_Key'

    # IV 64 bit
    IV = b'HelWorld'
    IV2 = IV

    # 18 bytes, for test
    M = b'Hello, How are you. Nice to meet you'
    M = get_padded_msg(M)  # (length becomes 24 in this case)

    n_rounds = getLength(M) // 8  # 3 (24 // 8)

    p_text = [M[i:i + 8] for i in range(0, len(M), 8)]  # split msg into 8 byte blocks each and store in list
    cipher_text = []

    c.send(str(n_rounds).encode())
    # print("rounds : ",n_rounds)

    # encryption
    for i in range(n_rounds):
        cipher = DES.new(key, DES.MODE_ECB)
        op = cipher.encrypt(IV)

        cipher_text.append(byte_xor(p_text[i], op))
        IV = op

    # send blocks
    for i in range(n_rounds):
        c.send(cipher_text[i])
        c.recv(1024).decode()   # just to gap between consecutive sends
    print("cipher blocks sent")
    c.close()
    break
