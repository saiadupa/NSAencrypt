def text(data):
    encrypted_text = ""
    for char in data:
        if char.isalpha():
            if char.isupper():
                encrypted_val = ord(char) - 64  
            else:
                encrypted_val = ord(char) - 96 + 26  
            encrypted_text += str(encrypted_val) + " "
        elif char == '!=':
            encrypted_text += 'D! '
        elif char == '@':
            encrypted_text += 'ade '
        else:
            encrypted_text += char + " "

    return encrypted_text.strip() 


def decrypt_text(data):
    decrypted_text = ""
    encrypted_values = data.split()

    for value in encrypted_values:
        if value.isdigit():
            num = int(value)
            if 1 <= num <= 26:
                decrypted_text += chr(num + 64)
            elif 27 <= num <= 52:
                decrypted_text += chr(num - 26 + 96)
        elif value == 'D!':
            decrypted_text += '!='
        elif value == 'ade':
            decrypted_text += '@'
        else:
            decrypted_text += value

    return decrypted_text
