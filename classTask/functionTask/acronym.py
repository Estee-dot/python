def acronym():
	acronym = " "
    letters = word.split()
    for letter in letters:
        acronym += letter[0]
    return acronym

name = input("Give a word: ")
print(acronym(words)) 




