import random

def DecimalToBinary(n):
    if n >= 1:
        DecimalToBinary(n // 2)
    print(n % 2, end='')

def ConvertToString(Binary):
    resultToChar = [chr(int(Binary[i:i + 8], 2)) for i in range(0, len(Binary), 8)]
    resultText = ""
    for letter in resultToChar:
        resultText = resultText + letter
    return resultText


def GenerateKey(Length):
    KeyList = []
    for _ in range(Length):
        bit = random.randint(0, 1)
        KeyList.append(str(bit))

    return ''.join(KeyList)


def ConvertToBinary(Block):
    messageList = []
    for character in Block:
        messageList.append(format(ord(character), '08b'))
    return ''.join(messageList)


# the round function used
def xor(a, b):
    output = ""
    for i in range(len(a)):
        inter = int(a[i]) + int(b[i])
        if inter == 2: inter = 0
        output = output + str(inter)

    return output

