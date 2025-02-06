import string


def encrypt_text_2(text, key):
    encrypt_text = ''
    for char in text:
        if char.islower():
            alphabet = string.ascii_lowercase
            index = alphabet.index(char)
            shifted_index = (index + key) % 26
            shifted_alphabet = alphabet[shifted_index]
            encrypt_text += shifted_alphabet
        elif char.isupper():
            alphabet = string.ascii_uppercase
            index = alphabet.index(char)
            shifted_index = (index + key) % 26
            shifted_alphabet = alphabet[shifted_index]
            encrypt_text += shifted_alphabet
        else:
            encrypt_text += char
    return encrypt_text


