from hashlib import sha256

def hashing(r, M):
    haash = sha256()
    haash.update(str(r).encode())
    haash.update(M.encode())
    return int(haash.hexdigest(), 16)

def verify(S1, S2, e1, e2, M, p):
    temp_v = (pow(e1, S2, p) * pow(e2, S1, p)) % p
    V = hashing(temp_v, M) % p

    if str(S1) == str(V):
        print("Signature Verified")
    else:
        print("wrong")
