#def get_vowels_removed(words):
    #vowels = "A", "a", "E", "e", "I", "i", "O", "o", "U", "u"
    #count = 0
    #for vowel in vowels:
        #for character in words:
            #if vowel != character:
                #character.remove()
    #return character


def get_vowels_removed(words):
	return[word.remove() for word in words]