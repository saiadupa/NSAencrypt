import os

def encrypt_image(image_path, key):
    with open(image_path, 'rb') as image_file:
        image_data = image_file.read()

    encrypted_data = bytearray()
    key_index = 0

    for byte in image_data:
        encrypted_byte = byte ^ ord(key[key_index % len(key)])
        encrypted_data.append(encrypted_byte)
        key_index += 1

    encrypted_dir = os.path.dirname(image_path)
    encrypted_image_path = os.path.join(encrypted_dir, 'encrypted_' + os.path.basename(image_path))
    with open(encrypted_image_path, 'wb') as encrypted_image:
        encrypted_image.write(encrypted_data)

    return encrypted_image_path 

def decrypt_image(encrypted_image_path, key):
    with open(encrypted_image_path, 'rb') as encrypted_image_file:
        encrypted_data = encrypted_image_file.read()

    decrypted_data = bytearray()
    key_index = 0

    for byte in encrypted_data:
        decrypted_byte = byte ^ ord(key[key_index % len(key)])
        decrypted_data.append(decrypted_byte)
        key_index += 1

    decrypted_dir = os.path.dirname(encrypted_image_path)
    decrypted_image_path = os.path.join(decrypted_dir, 'decrypted_' + os.path.basename(encrypted_image_path))
    with open(decrypted_image_path, 'wb') as decrypted_image:
        decrypted_image.write(decrypted_data)

    return decrypted_image_path 


