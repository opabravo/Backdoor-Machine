from Crypto.Cipher import AES
import os


def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")


def decrypt_file(file, key):
    with open(file, 'rb') as f:
        ciphertext = f.read()
    decr = decrypt(ciphertext, key)
    with open(os.path.basename(file)[:-12] + "_decrypted.txt", 'wb+') as f:
        f.write(decr)
    return os.path.basename(file)[:-12] + "_decrypted.txt"


def main():
    filepath = input("Input the path to the file to decrypt: ")
    key = input("Input the decryption key: ").encode()
    
    filename = decrypt_file(filepath, key)
    print(f"The decryption was successful. You can now open the file: {filename}")


main()