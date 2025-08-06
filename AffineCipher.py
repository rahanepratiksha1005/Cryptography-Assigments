from math import gcd

# Function to check if 'a' is coprime with 26
def is_coprime(a):
    return gcd(a, 26) == 1

# Encryption function
def affine_encrypt(text, a, b):
    if not is_coprime(a):
        raise ValueError("'a' must be coprime with 26")

    result = ""

    for ch in text:
        if ch.isalpha():
            offset = ord('A') if ch.isupper() else ord('a')
            x = ord(ch) - offset
            encrypted = (a * x + b) % 26
            result += chr(encrypted + offset)
        else:
            result += ch  # Keep spaces/punctuation unchanged

    return result

# Example usage
if __name__ == "__main__":
    print("\n Affine Cipher")
    plaintext = input("Enter plaintext: ")
    a = int(input("Enter key 'a' (must be coprime with 26): "))
    b = int(input("Enter key 'b': "))

    try:
        encrypted_text = affine_encrypt(plaintext, a, b)
        print("\nEncrypted text:", encrypted_text)
    except ValueError as ve:
        print("Error:", ve)
