import hashlib
import ctypes as c


def getHash(plaintext):
    b = plaintext.encode('ascii')
    result = hashlib.md5(b)
    byte = result.hexdigest()
    array2 = [0x00, 0x00, 0x00, 0x00]
    arraylist = []
    i = 0
    while i < len(byte) - 1:
        arraylist.append(int(byte[i] + byte[i + 1], 16))
        i += 2
    i = 0
    while i < 4:
        array2[0] = (array2[0] ^ arraylist[i * 4])
        array2[1] = (array2[1] ^ arraylist[i * 4 + 1])
        array2[2] = (array2[2] ^ arraylist[i * 4 + 2])
        array2[3] = (array2[3] ^ arraylist[i * 4 + 3])
        i += 1
    array2[0] = ((array2[0] & 1) | 2)
    encode = c.c_int32(array2[0]).value << 24 | c.c_int32(array2[1]).value << 16 \
             | c.c_int32(array2[2]).value << 8 | c.c_int32(array2[3]).value
    return encode


def calcula(imei):
    std1 = "5e8dd316726b0335"
    std2 = "97b7bc6be525ab44"
    encode1 = getHash(imei + std1)
    encode2 = getHash(imei + std2)
    print("Huawei Unlock CODE: {}".format(encode1))
    print("Huawei Flash CODE: {}".format(encode2))


if __name__ == '__main__':
    IMEI = "352375047353677"  # YOUR IMEI GO HERE
    calcula(imei=IMEI)
