class Narudzba:
    def __init__(self):
        self.proizvodi = []
        self.ukupna_cijena = 0


def napravi_narudzbu(svi_proizvodi, lista):
    if (type(lista) is not list) or (len(lista) == 0):
        print("Narudžba mora sadržavati barem jedan proizvod!")
        return None
    for item in lista:
        if (type(item) is not dict):
            print("Proizvod mora biti u obliku rječnika!")
            return None
        if "naziv" not in item or "kolicina" not in item or "cijena" not in item:
            print("Proizvod mora sadržavati ključeve 'naziv', 'kolicina' i 'cijena'!")
            return None
        naziv, kolicina = item["naziv"], item["kolicina"]
        if not any(proizvod.naziv == naziv and proizvod.kolicina >= kolicina for proizvod in svi_proizvodi):
            print(f"Proizvod {naziv} nije dostupan u traženoj količini!")
            return None

    narudzba = Narudzba()
    narudzba.proizvodi = lista
    narudzba.ukupna_cijena = sum(
        item["cijena"] * item["kolicina"] for item in lista
    )
    print("Narudžba uspješno kreirana!")
    return narudzba
