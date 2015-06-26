"""
* @name encrypt.py
*
* @author ahda86@gmail.com
*
* @date 2015/6/25 19:17
*
* @desc encrypt.py
"""

import random

def __mask(src):
    mask = 108

    buffSize = len(src)
    if buffSize == 0:
        return

    maxIdx = buffSize - 1
    for i in range(0, buffSize, 2):
        if i == maxIdx:
            src[i] ^= mask
            return

        bi = src[i]
        bj = src[i + 1]

        bi ^= mask
        bj ^= mask

        src[i] = bj
        src[i + 1] = bi

def __encrypt(src):
    buffSize = len(src)

    if buffSize == 0:
        return

    pivot = random.randint(1, 127)
    for i in range(buffSize):
        src[i] ^= pivot
        pivot = src[i]

    src.append(pivot)

def __decrypt(src):
    buffSize = len(src)

    if buffSize == 0:
        return

    pivot = src[-1]
    for i in range(buffSize - 1):
        src[i] ^= pivot

    del src[-1]

def simpleEncrypt(src):
    dest = list(src)
    __mask(dest)
    __encrypt(dest)

    return bytes(dest)

def simpleDecrypt(src):
    dest = list(src)

    __decrypt(dest)
    __mask(dest)

    return bytes(dest)

