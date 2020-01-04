import datetime
import hashlib
import binascii
import string
import ctypes

lib = ctypes.cdll.LoadLibrary('./libPoW.so')
lib.PoW.restype = ctypes.c_char_p
lib.PoW.argtypes = [ctypes.c_char_p, ctypes.c_char_p]


chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

def goPoW(target, algorithm):
    return lib.PoW(target, algorithm)

def pyPoW(target, algorithm):
    for ch1 in chars:
        for ch2 in chars:
            for ch3 in chars:
                for ch4 in chars:
                    s = ch1 + ch2 + ch3 + ch4
                    h = eval("hashlib.{1}(b'{0}').digest()".format(s, algorithm.decode()))
                    h = binascii.hexlify(h)
                    if h[len(h) - len(target):] == target:
                        return s
    return None


def benchmark(s, algorithm): # (bytes, bytes)
    print("[*] TARGET: {0}, ALGORITHM: {1}".format(s.decode(), algorithm.decode()))
    begin = datetime.datetime.now()
    res = goPoW(s, algorithm)
    end = datetime.datetime.now()
    print("\tGo PoW: time = {} usec".format((end - begin).microseconds))

    begin = datetime.datetime.now()
    res = pyPoW(s, algorithm)
    end = datetime.datetime.now()
    print("\tPy PoW: time = {} usec".format((end - begin).microseconds))


benchmark(b"abcd", b"sha1")
benchmark(b"abcd", b"sha256")
benchmark(b"abcd", b"md5")
benchmark(b"dead", b"sha1")
benchmark(b"dead", b"sha256")
benchmark(b"dead", b"md5")
