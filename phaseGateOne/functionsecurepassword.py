#pseudo code: passwords
#- Create a password generator function
#- password must have lowercase letters
#- password must have uppercase letters
#- password must contain numbers
#- password must contain symbols
#- len(password) == 16 characters

import random
import string

def get_secure_password():
	alphabet_lower = [i for i in string.ascii_lowercase]
	symbols = [i for i in string.punctuation]
	number = [i for i in string.digits]
	alphabet_upper = [i for i in string.ascii_uppercase]

	password = ""
	for _ in range(4):
		password += random.choice(alphabet_lower)
		password += random.choice(symbols)
		password += random.choice(number)
		password += random.choice(alphabet_upper)
	print(password)
	return random.shuffle(password)
	
print(get_secure_password())