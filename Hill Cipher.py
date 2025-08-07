import numpy as np
import math

def get_key_matrix_from_string(key):
    key = key.upper().replace("J", "I")
    key = ''.join(filter(str.isalpha, key))  # Remove non-letters
    length = len(key)
    n = int(math.sqrt(length))

    if n * n != length:
        raise ValueError("Key length must be a perfect square (4, 9, 16, ...).")

    key_nums = [ord(char) - ord('A') for char in key]
    key_matrix = np.array(key_nums).reshape(n, n)
    return key_matrix

def process_plaintext(text, n):
    text = text.upper().replace("J", "I")
    text = ''.join(filter(str.isalpha, text))
    padding_length = (n - len(text) % n) % n
    text += 'X' * padding_length
    return text

def encrypt(text, key_matrix):
    cipher = ""
    n = key_matrix.shape[0]

    for i in range(0, len(text), n):
        block = [ord(char) - ord('A') for char in text[i:i+n]]
        block_vector = np.array(block)
        result_vector = np.dot(key_matrix, block_vector) % 26
        cipher += ''.join(chr(num + ord('A')) for num in result_vector)

    return cipher

def main():
    print("HILL CIPHER ALGORITHM")
    key = input("Enter the key string (length must be a perfect square like 4, 9, 16...): ")

    try:
        key_matrix = get_key_matrix_from_string(key)
    except ValueError as e:
        print("Error:", e)
        return

    n = key_matrix.shape[0]
    print("Key Matrix:")
    print(key_matrix)

    plaintext = input("Enter the Plaintext: ")
    plaintext = process_plaintext(plaintext, n)
    print("Processed Plaintext:", plaintext)

    cipher_text = encrypt(plaintext, key_matrix)
    print("Cipher Text:", cipher_text)

if __name__ == "__main__":
    main()
