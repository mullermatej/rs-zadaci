lozinka = input("Unesi lozinku: ")


def provjera_lozinke(lozinka):
    if len(lozinka) < 8 or len(lozinka) > 15:
        print("Lozinka mora sadržavati između 8 i 15 znakova")
    elif not any(char.isdigit() for char in lozinka) or not any(char.isupper() for char in lozinka):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
    elif "password" in lozinka.lower() or "lozinka" in lozinka.lower():
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
    else:
        print("Lozinka je jaka!")


provjera_lozinke(lozinka)
