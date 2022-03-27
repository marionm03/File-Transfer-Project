from Crypto.Cipher import AES

key = b'12345678abcdefgh'
cipher = AES.new(key, AES.MODE_EAX)
filename = 'test.txt'

nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(filename)