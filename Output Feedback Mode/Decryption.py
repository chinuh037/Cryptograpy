import socket
from utils import getLength, byte_xor, get_padded_msg
from Crypto.Cipher import DES

s = socket.socket()
port = 12345
s.connect(('127.0.0.1', port))
print(f"Connected.")

key = b'I_am_Key'

# IV 64 bit
IV = b'HelWorld'

cipher_text = []
decode_text = []

n_rounds = s.recv(1024).decode()

# receive blocks
for i in range(int(n_rounds)):
    cipher_text.append(s.recv(1024))
    s.send("send another element".encode())     # just to gap between consecutive receives
print("cipher blocks received")

# decryption
for i in range(int(n_rounds)):
    cipher = DES.new(key, DES.MODE_ECB)
    op = cipher.encrypt(IV)

    decode_text.append(byte_xor(cipher_text[i], op))
    IV = op


msg_decrypt = b''
for i in range(int(n_rounds)):
    # print(decode_text[i])
    msg_decrypt = msg_decrypt + decode_text[i]

print("decrypted msg: ",str(msg_decrypt))
s.close()