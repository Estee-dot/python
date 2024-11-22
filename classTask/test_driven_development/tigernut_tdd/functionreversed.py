def get_string_reversed(text):

    reversed = ""
    for letter in text:
        reversed = letter + reversed
    return reversed