def vigenere_encrypt(plaintext, keyword):
    """
    Encrypts the plaintext using the Vigenère cipher with the given keyword.
    """
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    keyword_repeated = (keyword * (len(plaintext) // len(keyword))) + keyword[:len(plaintext) % len(keyword)]

    print(f"\nPlaintext: {plaintext}")
    print(f"Keyword Repeated: {keyword_repeated}")

    ciphertext = []
    for p, k in zip(plaintext, keyword_repeated):
        shift = (ord(p) - ord('A') + ord(k) - ord('A')) % 26
        encrypted_char = chr(shift + ord('A'))
        ciphertext.append(encrypted_char)

        print(f"Plaintext char: {p}, Keyword char: {k}, Shift: {shift}, Ciphertext char: {encrypted_char}")

    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, keyword):
    """
    Decrypts the ciphertext using the Vigenère cipher with the given keyword.
    """
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    keyword_repeated = (keyword * (len(ciphertext) // len(keyword))) + keyword[:len(ciphertext) % len(keyword)]

    print(f"\nCiphertext: {ciphertext}")
    print(f"Keyword Repeated: {keyword_repeated}")

    plaintext = []
    for c, k in zip(ciphertext, keyword_repeated):
        shift = (ord(c) - ord('A') - (ord(k) - ord('A')) + 26) % 26
        decrypted_char = chr(shift + ord('A'))
        plaintext.append(decrypted_char)

        print(f"Ciphertext char: {c}, Keyword char: {k}, Shift: {shift}, Plaintext char: {decrypted_char}")

    return ''.join(plaintext)

# User Input
plaintext = input("Enter the plaintext: ").replace(" ", "").upper()
keyword = input("Enter the keyword: ").replace(" ", "").upper()

# Encryption
print("\nEncryption Process:")
ciphertext = vigenere_encrypt(plaintext, keyword)
print(f"\nCiphertext: {ciphertext}")

# Decryption
print("\nDecryption Process:")
decrypted_text = vigenere_decrypt(ciphertext, keyword)
print(f"\nDecrypted Text: {decrypted_text}")
