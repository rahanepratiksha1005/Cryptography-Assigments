def caesar_encrypt(plaintext, key):
    ciphertext = ""

    for ch in plaintext:
        if ch.isupper():
            ciphertext += chr(((ord(ch) - ord('A') + key) % 26) + ord('A'))
        elif ch.islower():
            ciphertext += chr(((ord(ch) - ord('a') + key) % 26) + ord('a'))
        else:
            ciphertext += ch  # keep punctuation/space

    return ciphertext

def caesar_decrypt(ciphertext, key):
    plaintext = ""

    for ch in ciphertext:
        if ch.isupper():
            plaintext += chr(((ord(ch) - ord('A') - key + 26) % 26) + ord('A'))
        elif ch.islower():
            plaintext += chr(((ord(ch) - ord('a') - key + 26) % 26) + ord('a'))
        else:
            plaintext += ch  # keep punctuation/space

    return plaintext
print("\n Ceasor Cipher")
# Input from user
plaintext = input("Enter plaintext: ")
key = int(input("Enter key (0-25): "))

# Encrypt and Decrypt
encrypted = caesar_encrypt(plaintext, key)
decrypted = caesar_decrypt(encrypted, key)

print("\nEncrypted text:", encrypted)
print("Decrypted text:", decrypted)