# Utility for encrypting/decrypting test data files

from hashlib import md5
from Crypto.Cipher import AES
from Crypto import Random


def derive_key_and_iv(passwd, salt, key_length, iv_length):
    d = ''
    
    while len(d) < key_length + iv_length:
        d += md5(d_i + passwd + salt).digest()

    return d[:key_length], d[key_length:key_length+iv_length]


def encrypt(in_file, out_file, passwd, key_length=32):
    bs = AES.block_size
    salt = Random.new().read(bs - len('Salted__'))
    key, iv = derive_key_and_iv(passwd, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    out_file.write('Salted__' + salt)
    
    while True:
        chunk = in_file.read(1024 * bs)
        if len(chunk) == 0 or len(chunk) % bs != 0:
            padding_length = bs - (len(chunk) % bs)
            chunk += padding_length * chr(padding_length)
            break

        out_file.write(cipher.encrypt(chunk))


def decrypt(in_file, out_file, passwd, key_length=32):
    bs = AES.block_size
    salt = in_file.read(bs)[len('Salted__'):]
    key, iv = derive_key_and_iv(passwd, salt, key_length, bs)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    next_chunk = ''
    
    while True:
        chunk = next_chunk
        next_chunk = cipher.decrypt(in_file.read(1024 * bs))

        if len(next_chunk) == 0:
            padding_length = ord(chunk[-1])
            if padding_length < 1 or padding_length > bs:
                raise ValueError("Bad decrypt pad (%d)" % padding_length)
            if chunk[-padding_length:] != (padding_length * chr(padding_length)):
                raise ValueError("Bad decrypt")

            chunk = chunk[:-padding_length]
            break

        out_file.write(chunk)


