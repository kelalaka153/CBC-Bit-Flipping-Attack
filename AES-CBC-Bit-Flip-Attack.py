# The code is modified from
# https://gist.github.com/lopes/168c9d74b988391e702aac5f4aa69e41
#
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decrypt(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)
    
def bitFlip( pos, bit, data):
    raw = b64decode(data)

    list1 = list(raw)
    list1[pos] = chr(ord(list1[pos])^bit)
    raw = ''.join(list1)
    return b64encode(raw)


if __name__ == '__main__':

    key = b'Sixteen byte key'
    msg = "Buy 1000 lots of waffles"
    
    print('Original Message:', msg)

    ctx = AESCipher(key).encrypt(msg).decode('utf-8')
    print('Ciphertext      :', ctx)

    ctx = bitFlip(4,4,ctx)

    print('Message...      :', AESCipher(key).decrypt(ctx).decode('utf-8'))
