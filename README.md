
# Paillier Homomorphic Encryption Example

## Overview

This project demonstrates the basic usage of the **Paillier Homomorphic Encryption** scheme in Python using the `phe` library. Paillier is an additive homomorphic encryption system, which allows us to perform certain arithmetic operations directly on encrypted data without needing to decrypt it first. This feature enables secure computations on sensitive data while maintaining its confidentiality.

## Features

- **Key Generation**: Generate a public and private key pair.
- **Encrypted Addition**: Perform addition of encrypted numbers without decrypting them.
- **Encrypted Multiplication**: Multiply encrypted data by a scalar while keeping the data encrypted.

## Requirements

To use the project, you need to install the following dependencies:

```bash
pip install phe
```

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Annkkitaaa/Paillier-Homomorphic-Encryption.git
   cd Paillier-Homomorphic-Encryption
   ```

2. **Run the Script**:
   ```bash
   python paillier_encryption.py
   ```

3. **Example Output**:
   The script demonstrates the addition and multiplication of encrypted numbers.

   Example output:
   ```
   Generating keys...

   == Encrypted Addition ==
   Original numbers: 15, 25
   Decrypted sum: 40

   == Encrypted Multiplication ==
   Original number: 10, Scalar: 5
   Decrypted product: 50
   ```

## Functions

- **`initialize_keys()`**: Generates a pair of public and private keys for Paillier encryption.
- **`encrypt_data(public_key, data)`**: Encrypts a data point using the provided public key.
- **`decrypt_data(private_key, encrypted_data)`**: Decrypts encrypted data using the corresponding private key.
- **`perform_encrypted_addition(public_key, private_key, num1, num2)`**: Adds two encrypted numbers and returns the decrypted result.
- **`perform_encrypted_multiplication(public_key, private_key, num, scalar)`**: Multiplies an encrypted number by a scalar and returns the decrypted result.

## How It Works

The project uses the Paillier encryption scheme, which supports **additive homomorphism**. This allows us to:
- **Add encrypted values**: When two encrypted values are added, their plaintexts are added as well.
- **Multiply encrypted values by a scalar**: An encrypted number can be multiplied by a scalar without decrypting.

However, Paillier does not support direct multiplication of two encrypted values.

## Applications

Homomorphic encryption allows performing computations on encrypted data without revealing sensitive information, making it ideal for privacy-preserving tasks in fields such as:
- **Secure voting systems**
- **Encrypted financial computations**
- **Medical data processing**

