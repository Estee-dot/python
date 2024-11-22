def get_acronym(word):
    acronym = ""
    for letter in word:
        if letter == letter.upper:
            acronym += letter.strip()
    return acronym

