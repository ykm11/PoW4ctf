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

> vagrant/Ubuntu on macOS  
> Intel(R) Core(TM) i7-8850H CPU @ 2.60GHz 

| target |algorithm | Time Golang [usec]  | Time Python [usec] |
|---|---|---|---|
| dead  | sha1  | 8432  | 66340  |
|   | sha256  | 22816 | 148757 |
|   | sha224  | 60152 | 382477 |
|   | sha384  | 128164  | 747094 |
|   | sha512  | 144254 |  820544 |
| | md5  | 31199 | 269180 |
| beef  | sha1  | 39560  | 322154  |
|   | sha256  | 92983  | 606330 |
|   | sha224  | 30014  | 202007 |
|  | sha384  | 21930 | 123751 |
|  | sha512  | 40111 | 218024 |
|  | md5  | 4857 | 48344 |
