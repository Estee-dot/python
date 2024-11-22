def get_palindrome(text):
    reversed = ""
    for letter in text:
        reversed = letter + reversed
        if reversed == text:
            return True
        else:
            return False
