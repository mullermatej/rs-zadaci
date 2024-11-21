class Proizvod:
    naziv = ""
    cijena = 0
    kolicina = 0

    def __init__(self, naziv, cijena, kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.kolicina = kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, cijena: {
              self.cijena}, kolicina: {self.kolicina}")


def dodaj_proizvod(proizvod):
    proizvodi.append(proizvod)


proizvodi = [Proizvod("Mlijeko", 2.5, 100), Proizvod("Kruh", 1.5, 200)]
dodaj_proizvod(Proizvod("Jaja", 3, 50))

for proizvod in proizvodi:
    proizvod.ispis()
