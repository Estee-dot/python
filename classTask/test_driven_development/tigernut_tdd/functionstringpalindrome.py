#def get_string_palindrome(words):
	#return list(map(lambda letter: letter == letter[::-1], words))


#def get_string_palindrome(words):
	#result = []
	#for  word in words:
		#reversed = ""
		#for letter in word:
			#reversed = letter + reversed
		#if reversed == word:
			#result.append(True)
			
		#else: result.append(False)
	#return result


def get_string_palindrome(words):
    return [word == word[::-1] for word in words]

