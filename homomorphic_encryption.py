from phe import paillier

def initialize_keys():
    """Generates a public and private key pair for Paillier encryption."""
    public_key, private_key = paillier.generate_paillier_keypair()
    return public_key, private_key

def encrypt_data(public_key, data):
    """Encrypts a data point using the provided public key."""
    encrypted_data = public_key.encrypt(data)
    return encrypted_data

def decrypt_data(private_key, encrypted_data):
    """Decrypts encrypted data using the private key."""
    decrypted_data = private_key.decrypt(encrypted_data)
    return decrypted_data

def perform_encrypted_addition(public_key, private_key, num1, num2):
    """Performs addition on encrypted data without decrypting."""
    encrypted_num1 = encrypt_data(public_key, num1)
    encrypted_num2 = encrypt_data(public_key, num2)

    # Perform addition on encrypted data
    encrypted_sum = encrypted_num1 + encrypted_num2

    # Decrypt result
    decrypted_sum = decrypt_data(private_key, encrypted_sum)
    return decrypted_sum

def perform_encrypted_multiplication(public_key, private_key, num, scalar):
    """Performs multiplication of encrypted data with a scalar."""
    encrypted_num = encrypt_data(public_key, num)

    # Multiply encrypted number by a scalar
    encrypted_product = encrypted_num * scalar

    # Decrypt result
    decrypted_product = decrypt_data(private_key, encrypted_product)
    return decrypted_product

if __name__ == "__main__":
    # Step 1: Key generation
    print("Generating keys...")
    public_key, private_key = initialize_keys()

    # Example: Encrypted addition
    print("\n== Encrypted Addition ==")
    num1, num2 = 15, 25
    print(f"Original numbers: {num1}, {num2}")
    encrypted_sum = perform_encrypted_addition(public_key, private_key, num1, num2)
    print(f"Decrypted sum: {encrypted_sum}")

    # Example: Encrypted multiplication with a scalar
    print("\n== Encrypted Multiplication ==")
    num, scalar = 10, 5
    print(f"Original number: {num}, Scalar: {scalar}")
    encrypted_product = perform_encrypted_multiplication(public_key, private_key, num, scalar)
    print(f"Decrypted product: {encrypted_product}")
