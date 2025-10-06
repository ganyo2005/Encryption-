# 🔐 Text Encryptor & Decryptor (Python)

A simple Python program that **encrypts and decrypts text** using a randomly shuffled character mapping.  
This tool demonstrates basic cryptography logic using the `random` and `string` modules — perfect for beginners learning about substitution ciphers.

---

## ✨ Features

- 🔀 Randomly shuffles letters, digits, and punctuation to create a unique encryption key
- 🔒 Encrypts any input text character-by-character
- 🔓 Decrypts the encrypted text back to the original message
- 🧠 Simple and beginner-friendly design using classes

---

## 🧩 How It Works

1. The program builds a list of **all characters** (letters, digits, punctuation, and space).
2. It **creates a copy** of that list and shuffles it randomly — this becomes the encryption key.
3. When you enter text to encrypt:
   - Each character is replaced by the shuffled version at the same index.
4. When decrypting:
   - The process is reversed using the key to restore the original message.

---

## ⚙️ Requirements

- Python **3.8+** (works on Python 3.12 too)
- No external libraries — just Python’s built-in `random` and `string` modules

---

## 🚀 How to Run

### 🧱 1. Clone or copy the script

```bash
git clone https://github.com/yourusername/encryption.git
cd text-encryptor
```
