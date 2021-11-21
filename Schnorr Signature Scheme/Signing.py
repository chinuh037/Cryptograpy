import random
from hashlib import sha256

def hashing(r, M):
    haash = sha256()
    haash.update(str(r).encode())
    haash.update(M.encode())
    return int(haash.hexdigest(), 16)

def signing(e1, M, p, d):
    r = random.randint(1, p - 1)
    S1 = hashing(pow(e1, r, p), M) % p
    S2 = (r - (d * int(S1))) % (p - 1)

    return S1, S2