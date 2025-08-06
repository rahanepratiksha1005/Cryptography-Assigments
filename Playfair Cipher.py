def prepare_key_matrix(key):
    key = key.upper().replace("J", "I")
    result = []
    for char in key:
        if char not in result and char.isalpha():
            result.append(char)

    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
        if char not in result:
            result.append(char)

    # Create 5x5 matrix
    matrix = [result[i*5:(i+1)*5] for i in range(5)]
    return matrix

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def prepare_text(text, for_encryption=True):
    text = text.upper().replace("J", "I")
    prepared = ""
    i = 0
    while i < len(text):
        char1 = text[i]
        if not char1.isalpha():
            i += 1
            continue
        if i+1 < len(text):
            char2 = text[i+1]
            if not char2.isalpha():
                prepared += char1 + "X"
                i += 1
                continue
            if char1 == char2:
                prepared += char1 + "X"
                i += 1
            else:
                prepared += char1 + char2
                i += 2
        else:
            prepared += char1 + "X"
            i += 1
    return prepared

def encrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
    elif col1 == col2:
        return matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(matrix, a, b):
    row1, col1 = find_position(matrix, a)
    row2, col2 = find_position(matrix, b)

    if row1 == row2:
        return matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
    elif col1 == col2:
        return matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def playfair_encrypt(plaintext, key):
    matrix = prepare_key_matrix(key)
    plaintext = prepare_text(plaintext)
    ciphertext = ""

    for i in range(0, len(plaintext), 2):
        ciphertext += encrypt_pair(matrix, plaintext[i], plaintext[i+1])
    return ciphertext

def playfair_decrypt(ciphertext, key):
    matrix = prepare_key_matrix(key)
    plaintext = ""

    for i in range(0, len(ciphertext), 2):
        plaintext += decrypt_pair(matrix, ciphertext[i], ciphertext[i+1])
    return plaintext

# Example usage:
key = input("Enter key: ")
plaintext = input("Enter plaintext: ")

cipher = playfair_encrypt(plaintext, key)
print("Encrypted:", cipher)

decrypted = playfair_decrypt(cipher, key)
print("Decrypted:", decrypted)