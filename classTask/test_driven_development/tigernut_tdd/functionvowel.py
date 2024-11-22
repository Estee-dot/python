def get_vowel(word):
    vowels = "A", "a", "E", "e", "I", "i", "O", "o", "U", "u"
    count = 0
    for vowel in vowels:
        for character in word:
            if vowel == character:
                count += 1
    return count



