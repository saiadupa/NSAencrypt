import os

def encrypt_audio(audio_path, key):
    with open(audio_path, 'rb') as audio_file:
        audio_data = audio_file.read()

    encrypted_data = bytearray()
    key_index = 0

    for byte in audio_data:
        encrypted_byte = byte ^ ord(key[key_index % len(key)])
        encrypted_data.append(encrypted_byte)
        key_index += 1

    encrypted_dir = os.path.dirname(audio_path)
    encrypted_audio_path = os.path.join(encrypted_dir, 'encrypted_' + os.path.basename(audio_path))
    with open(encrypted_audio_path, 'wb') as encrypted_audio:
        encrypted_audio.write(encrypted_data)

    return encrypted_audio_path

def decrypt_audio(encrypted_audio_path, key):
    with open(encrypted_audio_path, 'rb') as encrypted_audio_file:
        encrypted_data = encrypted_audio_file.read()

    decrypted_data = bytearray()
    key_index = 0

    for byte in encrypted_data:
        decrypted_byte = byte ^ ord(key[key_index % len(key)])
        decrypted_data.append(decrypted_byte)
        key_index += 1

    decrypted_dir = os.path.dirname(encrypted_audio_path)
    decrypted_audio_path = os.path.join(decrypted_dir, 'decrypted_' + os.path.basename(encrypted_audio_path))
    with open(decrypted_audio_path, 'wb') as decrypted_audio:
        decrypted_audio.write(decrypted_data)

    return decrypted_audio_path 


