import random

from des import DesKey

sp = "/;/"
def padding(m):
    while len(m) % 8 != 0:
        m = m + " "
    return m

def remove_pad(m):
    rev = m[::-1]
    for i in range(len(m)):
        if rev[i] == " ":
            pass
        else:
            break
    m = rev[i:]
    m = m[::-1]

    return m


port = 12000

key = DesKey(b'chinuh03')

def xor_strings(A, B):
    A = A.encode()
    B = B.encode()

    res = bytes([a ^ b for a, b in zip(A, B)])
    return res.decode()

# get blocks
def get_b(m):
    b = []
    for i in range(0, len(m), 8):
        b.append(m[i:i+8])
    return b

# random key
def r_key(p):
    k = ""
    for i in range(p):
        t = str(random.randint(0,1))
        k = k + t
    return k

def Func(A, B, N):
    roll = 55
    roll2B = bin(roll)[2:].zfill(N)
    t = ""
    res = ""

    for i in range(N):
        if A[i] == B[i]:
            t = t + "0"
        else:
            t = t + "1"

    for i in range(N):
        if t[i] == roll2B[i]:
            res = res + "0"
        else:
            res = res + "1"

    return res

def XOR(i, j, n):
    t = ""
    for k in range(n):
        if i[k] == j[k]:
            t = t + "0"
        else:
            t = t + "1"

    return t

