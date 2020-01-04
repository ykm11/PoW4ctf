import ctypes
lib = ctypes.cdll.LoadLibrary('./libPoW.so')
lib.PoW.restype = ctypes.c_char_p
lib.PoW.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

def PoW(target, algorithm):
    res = lib.PoW(target, algorithm)
    return res

if __name__ == "__main__":
    s = b"dead"
    res = PoW(s, b"md5")
    print(res)
