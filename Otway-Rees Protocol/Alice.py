from Crypto import Random
import socket
from utils import padding, sp
import random
from datetime import datetime
from Crypto.Cipher import DES


def encrypt(msg1):
    des = DES.new(bytes(key_kdc.encode()), DES.MODE_OFB, IV)
    p_text = padding(msg1)
    cipher = IV + des.decrypt(p_text.encode())

    return public_m.encode() + sp.encode() + cipher

def toBob():
    IV = Random.new().read(DES.block_size)
    des_e = DES.new(sesh, DES.MODE_OFB, IV)
    pt = padding(msg)

    cip = IV + des_e.encrypt(pt.encode())

    s.send(cip)
    with open("update", "a") as f:
        f.write(datetime.now().isoformat() + "Finally Alice sent the message '{0}' to Bob\n".format(msg))


port = 12000
key_kdc = "helworld"

msg = "Hi Bob, How are you?"

s = socket.socket()
s.connect(('127.0.0.1', port))

# random
R = random.randrange(0, 1000)
RA = random.randrange(0, 1000)

IV = Random.new().read(DES.block_size)

with open("update", "w") as f:
    f.write(datetime.now().isoformat() + " Alice generated nonce R={0}, RA={1}\n".format(R, RA))

# encryption
public_m = "Alice,Bob,{0},".format(R)
m2En = public_m + str(RA)
s.send(encrypt(m2En))

with open("update", "a") as f:
    f.write(datetime.now().isoformat() + " Alice sent the request to BOB\n")

ticket = s.recv(1024)
with open("update", "a") as f:
    f.write(datetime.now().isoformat() + " Alice received her ticket from bob encrypted by alice key\n")


des_d = DES.new(bytes(key_kdc.encode()), DES.MODE_OFB, IV)
dec_ticket = des_d.decrypt(ticket)

R_rec, sesh = dec_ticket.split(sp.encode())
print("Sent to bob")
if int(R_rec) == RA:
    # now can send msg to bob
    toBob()
