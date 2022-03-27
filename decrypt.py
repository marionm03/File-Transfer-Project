from Crypto.Cipher import AES
import encrypt

key = b'12345678abcdefgh'
cipher = AES.new(key, AES.MODE_EAX, nonce=encrypt.nonce)
plaintext = cipher.decrypt(encrypt.ciphertext)
try:
    cipher.verify(encrypt.tag)
    print("The message is authentic:", plaintext)
except ValueError:
     print("Key incorrect or message corrupted")