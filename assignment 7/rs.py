from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import bytes_to_long, long_to_bytes

# Function to generate RSA keys (private and public)
def generate_keys():
    key = RSA.generate(2048)  # RSA key size of 2048 bits
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return private_key, public_key

# Function to encrypt a plaintext message using RSA and converting it to a number
def rsa_encrypt(plaintext, public_key):
    rsa_key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    
    # Convert plaintext to bytes and then to a long number
    plaintext_bytes = plaintext.encode('utf-8')
    plaintext_number = bytes_to_long(plaintext_bytes)
    
    # Encrypt the plaintext number using RSA
    encrypted_message = cipher.encrypt(long_to_bytes(plaintext_number))
    return encrypted_message

# Function to decrypt an RSA encrypted message and convert it back to plaintext
def rsa_decrypt(encrypted_message, private_key):
    rsa_key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(rsa_key)
    
    # Decrypt the message and convert back to a long number
    decrypted_message_bytes = cipher.decrypt(encrypted_message)
    decrypted_message_number = bytes_to_long(decrypted_message_bytes)
    
    # Convert the number back to bytes and decode it to a string
    decrypted_message = long_to_bytes(decrypted_message_number).decode('utf-8')
    return decrypted_message

# Example usage
if __name__ == "__main__":
    # Generate RSA keys
    private_key, public_key = generate_keys()

    # Take plaintext message as input from the user
    message = input("Enter the message to encrypt: ")

    # Encrypt the message
    encrypted_message = rsa_encrypt(message, public_key)
    print(f"Encrypted Message (in bytes): {encrypted_message}")

    # Decrypt the message
    decrypted_message = rsa_decrypt(encrypted_message, private_key)
    print(f"Decrypted Message: {decrypted_message}")
