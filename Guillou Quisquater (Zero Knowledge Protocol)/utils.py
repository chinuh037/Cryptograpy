# Euclidean Algo to calculate gcd
def gcd(n, m):
    if m == 0:
        return n

    return gcd(m, n % m)


def extended_euclidean(a, b):
    # Base Case
    if b == 0:
        return 1, 0

    x1, y1 = extended_euclidean(b, a % b)

    y = x1 - (a // b) * y1
    x = y1

    return x, y


def get_RRSM_set(m):
    res = []
    res.append(1)
    for i in range(2, m):

        g = gcd(i, m)
        if g == 1:
            res.append(i)

    return res


def multiplicative_inverse(a, m):  # to get multiplicative inverse of a under modulo m

    if gcd(a, m) == 1:

        x, y = extended_euclidean(a, m)
        inv = (x + m) % m
        return inv
    else:
        return -1
