from Crypto.Util import number
import math


def phi(m):
    if checkPrime(m):
        return m - 1
    ct = 0
    for i in range(1, m):
        if coprimes(i, m):
            ct += 1
    return ct


def euclidean(a, b):
    if a == 0:
        return b
    return euclidean(b % a, a)


# get prime factors of a
def get_prime_facs(a):
    s = set()

    for i in range(2, int(math.sqrt(a)) + 1):

        while a % i == 0:
            s.add(i)
            a = a // i

    if a > 2:
        s.add(a)

    return list(s)


def coprimes(a, b):
    if euclidean(a, b) == 1:
        return True
    else:
        return False


def checkPrime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1 or n == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def primitiveRoot(m):
    Phi = phi(m)
    divisors = get_prime_facs(Phi)

    for i in range(1, m):
        flag = True

        for div in divisors:
            if pow(i, Phi // div, m) == 1:
                flag = False

        if flag:
            return i
    return -1


def extendedE(a, m):
    if a == 0:
        return m, 0, 1

    gcd, x1, y1 = extendedE(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return gcd, x, y


def inverse(a, m):
    # print("Y",end = ' ')
    _, x, y = extendedE(a, m)
    inv = (x + m) % m
    return int(inv)


P_Bits = 20
Digest_Bits = 6


def generate_keys():

    p = number.getPrime(P_Bits)
    ls = get_prime_facs(p - 1)
    q = max(ls)

    e0 = primitiveRoot(p)
    e1 = pow(e0, (p - 1) // q, p)

    d = number.getPrime(P_Bits)  # private key
    e2 = pow(e1, d, p)

    public_k = (p, e1, e2)       # public key
    return public_k, d
