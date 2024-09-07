def caesar_cipher(message, shift, encrypt):
    result = ""
    for char in message:
        if char.isalpha():
            ascii_offset = ord('A') if char.isupper() else ord('a')
            new_pos = (ord(char) - ascii_offset + shift * (1 if encrypt else -1)) % 26
            new_char = chr(new_pos + ascii_offset)
            result += new_char
        else:
            result += char
    return result

# User input
message = input("Enter the message: ")
shift = int(input("Enter the shift value (1-25): "))
encrypt_decrypt = input("Type 'e' for encryption or 'd' for decryption: ")

if encrypt_decrypt.lower() == 'e':
    encrypted_message = caesar_cipher(message, shift, True)
    print("Encrypted message:", encrypted_message)
elif encrypt_decrypt.lower() == 'd':
    decrypted_message = caesar_cipher(message, shift, False)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice. Please enter 'e' for encrypt or 'd' for decrypt.")