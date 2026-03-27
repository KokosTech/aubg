str_inp = input("Enter a string: ")

def encrypt_string(string: str) -> str:
    encrypted = ""
    
    for char in string:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + 1) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
    
    return encrypted
    
    
def decrypt_string(string: str) -> str:
    decrypted = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                decrypted += chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
            else:
                decrypted += chr((ord(char) - ord('A') - 3) % 26 + ord('A'))
    
    return decrypted

encrypted_str = encrypt_string(str_inp)
print(f"Encrypted string: {encrypted_str}")
decrypted_str = decrypt_string(encrypted_str)
print(f"Decrypted string: {decrypted_str}")