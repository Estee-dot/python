#pseudo code:
#Create an empty String called encrypt_text
#using for loop, iterate through text
#compare if small letter 'a' is less than or equal to char and small letter 'z'
#if yes,using chr method, take in the string representation of unicode value
# of the inputted character and subtract it the unicode representation of 'a'
# Shift the character 13 times by adding 13 and divide by 26(alphabets count)
#add the result to the unicode value of index 'a'
#else if capital letter 'A' less than or equal to char and small letter 'Z'
#repeat the same
#else encrypt_text plus equal char
#else return encrypt_text
import string


def encrypt_text(text):
    encrypt_text = ''
    for char in text:
        if 'a' <= char <= 'z':
            encrypt_text += chr(((ord(char) - ord('a') + 13) % 26) + ord('a'))
        elif 'A' <= char <= 'Z':
            encrypt_text += chr(((ord(char) - ord('A') + 13) % 26) + ord('A'))
        else:
            encrypt_text += char

    return encrypt_text

