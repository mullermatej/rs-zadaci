def count_vowels_consonants(tekst):
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    rjecnik = {"vowels": 0, "consonants": 0}
    for char in tekst:
        if (char in vowels):
            rjecnik["vowels"] += 1
        elif (char in consonants):
            rjecnik["consonants"] += 1
    return rjecnik


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python jevrlo popularan."

print(count_vowels_consonants(tekst))

# {'vowels': 30, 'consonants': 48}
