def generate_key(plaintext,keyword):
   key = []
   keyword = keyword.upper()
   j = 0  

   for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            key.append(keyword[j % len(keyword)])
            j += 1
        else:
            key.append(plaintext[i])  

   return ''.join(key)
    
def vigenere_encrypt(plaintext,keyword):
    plaintext = plaintext.upper()
    key = generate_key(plaintext,keyword)
    cipher_text = ""

    for p,k in zip(plaintext,key):
        if p.isalpha():
            enc_char = chr((ord(p)+ord(k)-2*ord('A'))%26 + ord('A'))
            cipher_text += enc_char
        else:
            cipher_text += p
    return cipher_text

if __name__ == "__main__":
    print("\n Vigenere Cipher")
    plaintext = input("Enter plaintext: ")
    keyword = input("Enter keyword: ")

    encrypted = vigenere_encrypt(plaintext,keyword)
    print("\nEncrypted Text: ",encrypted)
