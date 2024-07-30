def gcd(a, b):
    # Function to return the greatest common divisor (GCD) of a and b
    while b != 0:
        a, b = b, a % b
    return a

def is_coprime(a, m):
    # Function to check if 'a' and 'm' are coprimes
    return gcd(a, m) == 1

def mod_inverse(a, m):
    # Function to find the modular inverse of 'a' under modulo 'm' using the Extended Euclidean Algorithm
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"No modular inverse for {a} under modulo {m}")

def encrypt_affine(plaintext, a, b):
    # Check if 'a' is coprime with the alphabet size (26)
    if not is_coprime(a, 26):
        raise ValueError(f"'a' ({a}) must be coprime with 26.")
    
    # Initialize the ciphertext as an empty string
    ciphertext = ""
    
    # Iterate over each character in the plaintext
    for char in plaintext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            # Apply the affine transformation for encryption
            encrypted_char = chr(((a * (ord(char) - shift_base) + b) % 26) + shift_base)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    
    # Return the resulting ciphertext
    return ciphertext

def decrypt_affine(ciphertext, a, b):
    # Check if 'a' is coprime with the alphabet size (26)
    if not is_coprime(a, 26):
        raise ValueError(f"'a' ({a}) must be coprime with 26.")
    
    # Initialize the plaintext as an empty string
    plaintext = ""
    
    # Find the modular inverse of 'a' under modulo 26
    a_inv = mod_inverse(a, 26)
    
    # Iterate over each character in the ciphertext
    for char in ciphertext:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            # Apply the affine transformation for decryption
            decrypted_char = chr((a_inv * ((ord(char) - shift_base) - b) % 26 + 26) % 26 + shift_base)
            plaintext += decrypted_char
        else:
            plaintext += char
    
    # Return the resulting plaintext
    return plaintext

# Example usage
plaintext = "This Is Nahpi"
a = 5
b = 8

# Encrypt the plaintext with the given a and b
encrypted = encrypt_affine(plaintext, a, b)
print(f"Encrypted: {encrypted}")  # Example output should be something like "Ihhsgnphzxtif123"

# Decrypt the ciphertext with the same a and b
decrypted = decrypt_affine(encrypted, a, b)
print(f"Decrypted: {decrypted}")  # Output should be "AffineCipher123"