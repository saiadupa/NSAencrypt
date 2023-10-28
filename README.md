# NSAencrypt

**NSAencrypt** is a Python package that provides functionalities for encryption and decryption of images, video, text, and audio.

## Installation

You can install NSAencrypt using pip:

```bash
pip install NSAencrypt
```

## Usage

Here's an example of how to use different functionalities provided by NSAencrypt:

### Image Encryption and Decryption

```python
from NSAencrypt.image import encrypt_image, decrypt_image

# Encrypt an image
encrypted_image_path = encrypt_image(r'path\to\your\image.png', 'your_key')

# Decrypt the encrypted image
decrypted_image_path = decrypt_image(encrypted_image_path, 'your_key')
```

### Video Encryption and Decryption

```python
from NSAencrypt.video import encrypt_video, decrypt_video

# Encrypt a video
encrypted_video_path = encrypt_video(r'path\to\your\video.mp4', 'your_key')

# Decrypt the encrypted video
decrypted_video_path = decrypt_video(encrypted_video_path, 'your_key')
```

### Text Encryption and Decryption

```python
from NSAencrypt.text import encrypt_text, decrypt_text

# Encrypt text
encrypted_text = encrypt_text("Your secret message")

# Decrypt the encrypted text
decrypted_text = decrypt_text(encrypted_text)
```

### Audio Encryption and Decryption

```python
from NSAencrypt.audio import encrypt_audio, decrypt_audio

# Encrypt an audio file
encrypted_audio_path = encrypt_audio(r'path\to\your\audio.mp3', 'your_key')

# Decrypt the encrypted audio file
decrypted_audio_path = decrypt_audio(encrypted_audio_path, 'your_key')
```
