def obrni_rjecnik(rjecnik):
    novi_rjecnik = {}
    for rijec in rjecnik:
        vrijednost = rjecnik[rijec]
        novi_rjecnik[vrijednost] = rijec
    return novi_rjecnik


rjecnik = {"ime": "Ivan", "prezime": "Ivić", "dob": 25}

print(obrni_rjecnik(rjecnik))

# {'Ivan': 'ime', 'Ivić': 'prezime', 25: 'dob'}
