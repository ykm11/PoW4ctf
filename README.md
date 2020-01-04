# PoW4ctf  
md5, sha1, sha224, sha256, sha384, sha512に対応しています。


<br />
## 使い方  

ビルドしたらpythonから呼び出せるようになります。  
> go build -o libPoW.so -buildmode=c-shared proof_of_work.go

```
import ctypes
lib = ctypes.cdll.LoadLibrary('./libPoW.so')
lib.PoW.restype = ctypes.c_char_p
lib.PoW.argtypes = [ctypes.c_char_p, ctypes.c_char_p]

# ex (python3)
lib.PoW(b"abcd", b"sha1")
# >> b'aGPG'
```
