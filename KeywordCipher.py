import string 
def generate_cipher_alphabet(keyword):
    keyword = "".join(sorted(set(keyword), key=keyword.index))
    keyword = keyword.upper()
    alphabet = string.ascii_uppercase
    remaining_letters = "".join([ch for ch in alphabet if ch not in keyword])
    cipher_alphabet = keyword + remaining_letters
    return dict(zip(alphabet,cipher_alphabet))

def keyword_encrypt(plaintext,keyword):
    cipher_map = generate_cipher_alphabet(keyword)
    result = ""
    for ch in plaintext:
        if ch.isupper():
            result += cipher_map.get(ch, ch)
        elif ch.islower():
            result += cipher_map.get(ch.upper(), ch).lower()
        else:
            result += ch  # Keep punctuation/space unchanged

    return result

if __name__ == "__main__":
    print("\n Keyword Cipher ")
    plaintext = input("Enter Plaintext: ")
    keyword = input("Enter Keyword: ")
    encrypted = keyword_encrypt(plaintext,keyword)
    print("\n Encrypted Text: ",encrypted)
            
