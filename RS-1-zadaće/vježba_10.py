def brojanje_riječi(tekst):
    čisti_tekst = ""
    broj_riječi = {}
    for char in tekst:
        if char != ".":
            čisti_tekst += char
    tekst = čisti_tekst
    riječi = tekst.lower().split()
    for riječ in riječi:
        if (riječ in broj_riječi):
            broj_riječi[riječ] += 1
        else:
            broj_riječi[riječ] = 1
    return broj_riječi


tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(brojanje_riječi(tekst))
