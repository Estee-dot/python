
def encrypt_text(text):
        if 'a' <= char <= 'z':
            return chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            return chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            return char



