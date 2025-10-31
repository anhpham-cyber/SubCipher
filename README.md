# Substitution Cipher Tool

A Python monoalphabetic substitution cipher with a unique random key generated on every run. Encrypts and decrypts messages, exports the key for secure exchange. Ideal for CTF challenges, red team payload obfuscation, or blue team training in detecting classical encryption via frequency analysis.

---

## Features

- Encrypt any text message using a **random substitution key**  
- Decrypt messages encrypted with the generated key  
- Supports **letters, numbers, punctuation, and spaces**  
- Simple console interface for interactive use  

---

## How It Works

1. The program creates a **list of all characters**:  
   letters (uppercase & lowercase), digits, punctuation, and space.  
2. A **randomly shuffled copy** of this list becomes the encryption key.  
3. To **encrypt**, each character in the message is replaced with the character in the same position from the shuffled key.  
4. To **decrypt**, the program finds the index of each character in the key and replaces it with the original character from the standard list.  

---

## Example Run

Please enter your text: Hello World!

Original message: Hello World!

Encrypted message: q@A$% 3fLzW#


Please enter your encrypted message: q@A$% 3fLzW#

Encrypted message: q@A$% 3fLzW#

Original message: Hello World!

> Note: The encrypted message will be different each time because the key is randomly shuffled.

---

## Requirements

- Python 3.x  
- No external libraries required (uses only `random` and `string`)  

---

## Notes

- Only messages encrypted with the generated key can be correctly decrypted.  
- You can reuse the same key if you store it in a variable or a file, so messages can be decrypted later.  
- This is a beginner-friendly project to practice **lists, indexing, loops, and string manipulation** in Python.  

---

