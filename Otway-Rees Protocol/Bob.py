import random
from datetime import datetime
from Crypto import Random
from utils import padding, sp
from Crypto.Cipher import DES
import socket

key_kdc = "prajuh26"
Aport = 12000
Kport = 12345

def encrypt(m):
    des = DES.new(bytes(key_kdc.encode()), DES.MODE_OFB, IV)
    p_text = padding(m)
    cipher_t = IV + des.encrypt(p_text.encode())
    return cipher_t + sp.encode() + A_ticket

def sendMsg2KDC(msg_2_send):
    s = socket.socket()
    s.connect(('127.0.0.1', Kport))
    s.send(msg_2_send)

    with open("update", "a") as f:
        f.write(datetime.now().isoformat() + " Msg from Bob to KDC with tickets\n")

    message_recv = s.recv(1024)
    with open("update", "a") as f:
        f.write(datetime.now().isoformat() + " Bob received session key tickets\n")
    s.close()
    return message_recv


s = socket.socket()
s.bind(('', Aport))
s.listen(1)
print("Socket is listening")

while True:
    c, addr = s.accept()

    message_rec = c.recv(1024)

    public, A_ticket = message_rec.split(b'/;/')
    public = public.decode()[:-1]

    alice, bob, R = public.split(",")

    RB = random.randint(1, 20)
    IV = Random.new().read(DES.block_size)

    public_msg = "Alice,Bob,{0},".format(R)

    # encryption
    tickets = sendMsg2KDC(encrypt(public_msg + str(RB)))
    ticket = tickets.split(sp.encode())[-2]

    des_d = DES.new(bytes(key_kdc.encode()), DES.MODE_OFB, IV)
    decrypt_ticket = des_d.decrypt(ticket)

    R_rec, sesh = decrypt_ticket.split(sp.encode())
    c.send(tickets.split(sp.encode())[-1])

    with open("update", "a") as f:
        f.write(datetime.now().isoformat() + " Bob sent the message to Alice with session key = {0} and nonce RA\n".format(repr(sesh)))

    message = c.recv(1024)
    IV = message[:DES.block_size]
    cipher = message[DES.block_size:]

    des = DES.new(sesh.strip(), DES.MODE_OFB, IV)
    msg = des.decrypt(cipher)

    if int(R_rec) == RB:
        print("Alice authentication Successful")
        with open("update", "a") as f:
            f.write(datetime.now().isoformat() + " Alice is authenticated and Bob finally received the message = {0}\n".format(msg.decode()))
        print("Message from Alice: {0}".format(msg.decode()))

    c.close()
    print("connection closed")
    break
