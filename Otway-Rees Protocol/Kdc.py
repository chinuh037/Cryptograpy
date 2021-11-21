from datetime import datetime
import socket
from Crypto import Random
from utils import *
from Crypto.Cipher import DES

Port = 12345
B_Port = 12000

key_A = "helworld"
key_B = "prajuh26"

def get_Ticket(R, seshkey, IV, key):
    des = DES.new(key.encode(), DES.MODE_OFB, IV)
    mess = R.encode() + sp.encode() + seshkey

    return des.encrypt(mess)

def send_tickets(msg, c, IV):
    c.send(IV + msg)
    with open("update", "a") as f:
        f.write(datetime.now().isoformat() + " kdc sent the tickets to bob with session key \n")

s = socket.socket()
s.bind(('', Port))
s.listen(1)
print("Socket is Listening")

while True:
    c, addr = s.accept()
    print(f"Got connection from {addr}")

    data = c.recv(1024)
    with open("update", "a") as f:
        f.write(datetime.now().isoformat() + " kdc received the tickets from Bob \n")

    Bob_section, Alice_section = data.split(b'/;/')

    # Bob part
    IV_bob = Bob_section[:DES.block_size]
    des = DES.new(key_B.encode(), DES.MODE_OFB, IV_bob)
    Bob_decode = des.decrypt(Bob_section[DES.block_size:]).decode()
    _,_,R,R_Bob = Bob_decode.split(",")

    # Alice part
    IV_Alice = Alice_section[:DES.block_size]
    des = DES.new(key_A.encode(), DES.MODE_OFB, IV_Alice)
    Alice_decode = des.decrypt(Alice_section[DES.block_size:]).decode()
    _,_,_,R_Alice = Alice_decode.split(",")

    # alice and bob nonce
    R_Alice = R_Alice.strip()
    R_Bob = R_Bob.strip()

    sesh_key = Random.new().read(8)

    # get tickets
    bob_tkt = get_Ticket(R_Bob, sesh_key, IV_bob, key_B)
    alice_tkt = get_Ticket(R_Alice, sesh_key, IV_Alice, key_A)

    msg2BOB = R.encode() + sp.encode() + bob_tkt + sp.encode() + alice_tkt

    send_tickets(msg2BOB, c, IV_Alice)

    c.close()
    print("connection closed")
    break
