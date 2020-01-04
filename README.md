# PoW4ctf  
md5, sha1, sha224, sha256, sha384, sha512に対応しています。



# 使い方  

ビルドしたらpythonから呼び出せるようになります。  
> $ go build -o libPoW.so -buildmode=c-shared proof_of_work.go

```
import ctypes
lib = ctypes.cdll.LoadLibrary('./libPoW.so')
lib.PoW.restype = ctypes.c_char_p
lib.PoW.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

# ex (python3)
lib.PoW(b"abcd", b"sha1")
# >> b'aGPG'
binascii.hexlify(hashlib.sha1(b'aGPG').digest())
# >> b'9aa0a4592abf659c04b90973fb3dedf5d9c1abcd'
```


# Benchmark

| target |algorithm | Time Go [usec]  | Time Py [usec] |
|---|---|---|---|
| dead  | sha1  | 9771  | 96973  |
|   | sha256  | 19800 | 261932 |
|   | sha224  | 52616 | 681575 |
|   | sha384  | 113460  | 349599 |
|   | sha512  | 124306 |  455819 |
| | md5  | 29590 | 456840|
| beef  | sha1  | 40518  | 571753  |
|   | sha256  | 81564  | 54642 |
|   | sha224  | 25631  | 348169 |
|  | sha384  | 20159 | 215599 |
|  | sha512  | 36488 | 373933|
|  | md5  | 4576 |81304 |
