import string
import random

from Crypto.Cipher import AES


print(AES.block_size)
print(string.ascii_letters)
key = ''.join(random.choice(string.ascii_letters) for _ in range(AES.block_size))
print(key)

iv = ''.join(random.choice(string.ascii_letters) for _ in range(AES.block_size))

plaintext = 'fdiafejiwaifdjafewafeaf'
cipher = AES.new(key, AES.MODE_CBC, iv)
padding_length = AES.block_size - len(plaintext) % AES.block_size
plaintext += chr(padding_length) * padding_length
cipher_text = cipher.encrypt(plaintext)
print(cipher_text)

cipher2 = AES.new(key, AES.MODE_CBC, iv)
decrypted_text = cipher2.decrypt(cipher_text)
print(decrypted_text[:-decrypted_text[-1]])
