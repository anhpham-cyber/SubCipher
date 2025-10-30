import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()
print(chars)
print(key)

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

#ENCRYPT
plain_text = input("Please enter you text: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encryted message: {cipher_text}")

#DECRYPT
cipher_text = input("Please enter you encrypted message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]


print(f"Encryted message: {cipher_text}")
print(f"Original message: {plain_text}")
