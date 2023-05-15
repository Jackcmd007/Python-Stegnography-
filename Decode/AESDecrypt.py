from Crypto.Cipher import AES
import os

def Decrypt():
    input_file = 'encrypted.bin'
    key_path = 'C:/Users/justi/OneDrive/Desktop/Steganocrypt-master/Key/my_key.bin'


    with open(key_path, 'rb') as f:
        key = f.read()
        f.close()
        
    file_in = open(input_file, 'rb')
    iv = file_in.read(16)
    ciphered_data = file_in.read()
    file_in.close()

    cipher = AES.new(key, AES.MODE_CFB, iv=iv)
    original_data = cipher.decrypt(ciphered_data) # No need to un-pad

    print(original_data.hex())
    return original_data
