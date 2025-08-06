def atbash_cipher(text):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr(ord('Z') - (ord(ch) - ord('A')))
        elif ch.islower():
            result += chr(ord('z') - (ord(ch) - ord('a')))
        else:
            result += ch  # Keep punctuation/space

    return result

# Input from user
text = input("Enter text for Atbash Cipher: ")

# Encryption and Decryption are same in Atbash
ciphertext = atbash_cipher(text)
print("\n Atbash Cipher")
print("\nAtbash Ciphertext:", ciphertext)