package main
// go build -o libPoW.so -buildmode=c-shared proof_of_work.go
import (
    "C"
    "fmt"
    "hash"
    "strings"
    "crypto/MD5"
    "crypto/SHA1"
    "crypto/SHA256"
    "crypto/SHA512"
)

var (
    chars string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
)

func GetHash(val, algorithm string) []byte {
    var hashData []byte
    var hasher hash.Hash

    switch algorithm {
    case "md5", "MD5":
        hasher = md5.New()
    case "sha1", "SHA1":
        hasher = sha1.New()
    case "sha224", "SHA224":
        hasher = sha256.New224()
    case "sha256", "SHA256":
        hasher = sha256.New()
    case "sha384", "SHA384":
        hasher = sha512.New384()
    case "sha512", "SHA512":
        hasher = sha512.New()
    default:
        hasher = sha256.New()
    }

    hasher.Write([]byte(val))
    hashData = hasher.Sum(nil)
    return hashData
}

//export PoW
func PoW(target, algorthm *C.char) *C.char {
    var str, hashString string
    var tmp string
    for _, ch1  := range(chars) {
        for _, ch2  := range(chars) {
            for _, ch3  := range(chars) {
                for _, ch4  := range(chars) {
                    str = fmt.Sprintf("%s%s%s%s",
                        string(ch1), string(ch2), string(ch3), string(ch4))
                    hashString = fmt.Sprintf("%x", GetHash(str, C.GoString(algorthm)))
                    tmp = hashString[len(hashString)-len(C.GoString(target)):]
                    if strings.Compare(tmp, C.GoString(target)) == 0 {
                        return C.CString(str)
                    }
                }
            }
        }
    }
    return nil
}

func main() {
}
