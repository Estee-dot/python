def is_palindrome(text):
	reversed = ""
	for letter in text:
		reversed = letter + reversed

	if reversed == text:
		return True

	return False

message = input("Enter text: ")
print(is_palindrome(message))

