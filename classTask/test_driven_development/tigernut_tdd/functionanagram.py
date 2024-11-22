def get_Anagram(wordOne, wordTwo):
    for char in wordOne:
        if char in wordTwo:
            return True
        else:
            return false