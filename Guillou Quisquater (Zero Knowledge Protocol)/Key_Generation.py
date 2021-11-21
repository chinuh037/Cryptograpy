from Crypto.Util import number
import random

P_B = 12
Q_B = 6

# Euclidean Algo to calculate gcd
def gcd(a, b):
    if a == 0:
        return b

    return gcd(b % a, a)


def extended_euclidean(a, m):
    # Base Case
    if a == 0:
        return m, 0, 1

    Gcd, x1, y1 = extended_euclidean(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return Gcd, x, y


def multiplicative_inverse(a, m):

    _, x, y = extended_euclidean(a, m)
    inv = (x + m) % m
    return int(inv)

def get_RRSM_set(m):
    res = []
    res.append(1)
    for i in range(2, m):
        if gcd(i, m) == 1:
            res.append(i)

    return res

def key_generation():

    p = number.getPrime(P_B)
    q = number.getPrime(Q_B)

    n = p*q

    rrsm_n = get_RRSM_set(n)
    s = random.choice(rrsm_n)

    rrsm = get_RRSM_set((p-1)*(q-1))
    e = random.choice(rrsm)

    temp = pow(s,e,n)
    v = multiplicative_inverse(temp, n)

    return n, e, s, v






