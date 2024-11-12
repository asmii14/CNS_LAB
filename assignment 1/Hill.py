import numpy as np

def mod26_inverse(matrix):
    """
    Calculate the modular inverse of a 2x2 matrix under mod 26.
    """
    det = int(np.round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_mod26 = det % 26

    # Find modular inverse of determinant
    for i in range(1, 26):
        if (det_mod26 * i) % 26 == 1:
            det_inv = i
            break
    else:
        raise ValueError("No modular inverse exists for this matrix")

    # Adjugate matrix
    adjugate = np.array([[matrix[1][1], -matrix[0][1]], 
                         [-matrix[1][0], matrix[0][0]]])
    
    # Modular inverse matrix
    inv_matrix = (det_inv * adjugate) % 26
    return inv_matrix

def text_to_numbers(text):
    """
    Convert text to numbers (A=0, B=1, ..., Z=25)
    """
    return [ord(char) - ord('A') for char in text.upper()]

def numbers_to_text(numbers):
    """
    Convert numbers back to text (0=A, 1=B, ..., 25=Z)
    """
    return ''.join(chr(num + ord('A')) for num in numbers)

def hill_cipher_encrypt(plaintext, key_matrix):
    """
    Encrypt the plaintext using the Hill cipher with the given key matrix.
    """
    n = key_matrix.shape[0]
    if len(plaintext) % n != 0:
        plaintext += 'Z' * (n - len(plaintext) % n)
    
    plaintext_numbers = text_to_numbers(plaintext)
    ciphertext_numbers = []

    print(f"\nPlaintext Numbers: {plaintext_numbers}")

    for i in range(0, len(plaintext_numbers), n):
        block = plaintext_numbers[i:i+n]
        print(f"\nBlock: {block}")
        block_vec = np.array(block).reshape(-1, 1)
        print(f"Block Vector:\n{block_vec}")

        encrypted_vec = (key_matrix @ block_vec) % 26
        print(f"Encrypted Vector:\n{encrypted_vec}")
        ciphertext_numbers.extend(encrypted_vec.flatten().tolist())

    return numbers_to_text(ciphertext_numbers)

def hill_cipher_decrypt(ciphertext, key_matrix):
    """
    Decrypt the ciphertext using the Hill cipher with the given key matrix.
    """
    key_inv = mod26_inverse(key_matrix)
    ciphertext_numbers = text_to_numbers(ciphertext)
    plaintext_numbers = []

    print(f"\nCiphertext Numbers: {ciphertext_numbers}")

    n = key_matrix.shape[0]
    for i in range(0, len(ciphertext_numbers), n):
        block = ciphertext_numbers[i:i+n]
        print(f"\nBlock: {block}")
        block_vec = np.array(block).reshape(-1, 1)
        print(f"Block Vector:\n{block_vec}")

        decrypted_vec = (key_inv @ block_vec) % 26
        print(f"Decrypted Vector:\n{decrypted_vec}")
        plaintext_numbers.extend(decrypted_vec.flatten().tolist())

    return numbers_to_text(plaintext_numbers)

# User Input
plaintext = input("Enter the plaintext: ").upper()
key_matrix = []

print("Enter the 2x2 key matrix values row-wise:")
for i in range(2):
    row = list(map(int, input(f"Row {i+1}: ").split()))
    key_matrix.append(row)

key_matrix = np.array(key_matrix)

# Encrypt
print("\nEncryption Process:")
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print(f"\nCiphertext: {ciphertext}")

# Decrypt
print("\nDecryption Process:")
decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
print(f"\nDecrypted Text: {decrypted_text}")
