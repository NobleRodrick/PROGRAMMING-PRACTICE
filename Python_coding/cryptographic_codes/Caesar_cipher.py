def encrypt_caesar(plaintext, shift):
    #Initialize the ciphertext as an empty string
    cipher_text = ""
    # Iterate over each character in the plain text
    for char in plaintext:
        #check if the character is an alphabet letter
        if char.isalpha():
            # determine the base ASCII value based on uppercase or lowercase
            shift_base = 65 if char.isupper() else 97
            # shift the character by the given shift amount and wrap around using modulo 26
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            #append the encrypted character to the ciphertext
            cipher_text += encrypted_char
        else:
            # if the character is mot an alphabet letter, leave it unchanged
            cipher_text += char
            
    return cipher_text


def decrypt_caesar(cipher_text, shift):
    # initialize the plain text as empty string
    plain_text = ""
    #iterate over each character in the ciphertext
    for char in cipher_text:
        # check if the character is an alphabet letter
        if char.isalpha():
            # Determine the base ASCII value based on the uppercase or lowercase
            shift_base = 65 if char.isupper() else 97
            #shift the character back by the given shift amount and wrap around using modulo 26
            decrypted_char = chr((ord(char) - shift_base - shift) % 26 + shift_base)
            # append the decrypted character to the decrypted text
            plain_text += decrypted_char
        else:
            # if the character is not an alphabet, leave it unchanged
            plain_text += char
        
    return plain_text


# Example usage
plain_text = "HELLO"
shift = 3

# Encrypt the plain text with the given shift
encrypted = encrypt_caesar(plain_text, shift)
print(f"The encrypted form: {encrypted}") #output should be "KHOOR"

# Decrypt the ciphertext with the same shift
decrypted = decrypt_caesar(encrypted, shift)
print(f"The decrypted text is: {decrypted}")# output should be "HELLO"

     