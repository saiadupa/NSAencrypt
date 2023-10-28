import os

def encrypt_video(video_path, key):
    with open(video_path, 'rb') as video_file:
        video_data = video_file.read()

    encrypted_data = bytearray()
    key_index = 0

    for byte in video_data:
        encrypted_byte = byte ^ ord(key[key_index % len(key)])
        encrypted_data.append(encrypted_byte)
        key_index += 1

    encrypted_dir = os.path.dirname(video_path)
    encrypted_video_path = os.path.join(encrypted_dir, 'encrypted_' + os.path.basename(video_path))
    with open(encrypted_video_path, 'wb') as encrypted_video:
        encrypted_video.write(encrypted_data)

    return encrypted_video_path

def decrypt_video(encrypted_video_path, key):
    with open(encrypted_video_path, 'rb') as encrypted_video_file:
        encrypted_data = encrypted_video_file.read()

    decrypted_data = bytearray()
    key_index = 0

    for byte in encrypted_data:
        decrypted_byte = byte ^ ord(key[key_index % len(key)])
        decrypted_data.append(decrypted_byte)
        key_index += 1

    decrypted_video_path = os.path.join(os.path.dirname(encrypted_video_path), 'decrypted_' + os.path.basename(encrypted_video_path))
    with open(decrypted_video_path, 'wb') as decrypted_video:
        decrypted_video.write(decrypted_data)

    return decrypted_video_path

