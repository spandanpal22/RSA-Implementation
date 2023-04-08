# Using python library pycryptodome

from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def generate_key_pair():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()

    file_out = open("private.pem", "wb")
    file_out.write(private_key)
    file_out.close()

    file_out = open("public.pem", "wb")
    file_out.write(public_key)
    file_out.close()

    return private_key, public_key

def encrypt_message(message):
    with open('public.pem', mode='rb') as file:
        key = RSA.import_key(file.read())

    cipher = PKCS1_OAEP.new(key)
    encrypted_message = cipher.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message):
    with open('private.pem', mode='rb') as file:
        key = RSA.import_key(file.read())

    cipher = PKCS1_OAEP.new(key)
    decrypted_message = cipher.decrypt(encrypted_message).decode()
    return decrypted_message

# private_key, public_key = generate_key_pair()
# print("\nPublic Key: ", public_key)
# print("\nPrivate Key: ", private_key)

message = "Hello World!"
print("\nOriginal Message: ", message)

encrypted_message = encrypt_message(message)
print("\nEncrypted Message: ", encrypted_message)

decrypted_message = decrypt_message(encrypted_message)
print("\nDecrypted Message: ", decrypted_message)