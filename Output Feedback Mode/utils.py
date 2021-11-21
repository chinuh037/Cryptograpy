def getLength(a):
    b = 0
    for i in range(len(a)):
        b = b + 1

    return b


def get_block_size(a):
    R = 7
    for i in range(8):
        if a % R == 0:
            return R
        else:
            R = R-1


def byte_xor(ba1, ba2):
    return bytes([a ^ b for a, b in zip(ba1, ba2)])

# to pad msg in multiples of 8
def get_padded_msg(m):
    l = getLength(m)
    for i in range(100):
        if l < 8*i:
            l = 8*i - l
            break

    return m + l * b' '
