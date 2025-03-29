# Logic program.

import base64
import hashlib
import itertools
import string

def caesar_brute_force(ciphertext):
    results = []
    for shift in range(1, 26):
        decrypted = ""
        for char in ciphertext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                decrypted += chr((ord(char) - start - shift) % 26 + start)
            else:
                decrypted += char
        results.append(f"Shift {shift}: {decrypted}")
    return "\n".join(results)

def vigenere_decrypt(ciphertext, key):
    decrypted = ""
    key = key.lower()
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('a')
            start = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - start - shift) % 26 + start)
            key_index += 1
        else:
            decrypted += char
    return decrypted

def md5_brute_force(target_hash, max_length=4):
    chars = string.ascii_lowercase
    for length in range(1, max_length + 1):
        for attempt in itertools.product(chars, repeat=length):
            guess = ''.join(attempt)
            guess_hash = hashlib.md5(guess.encode()).hexdigest()
            if guess_hash == target_hash:
                return f"Ditemukan: {guess}"
    return "Tidak ditemukan (coba tingkatkan max_length)"

def base64_decode(text):
    try:
        return base64.b64decode(text.encode()).decode()
    except Exception as e:
        return f"Error decoding Base64: {e}"
