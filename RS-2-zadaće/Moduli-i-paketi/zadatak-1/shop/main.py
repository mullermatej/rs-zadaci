from proizvodi import Proizvod, dodaj_proizvod
from narudzbe import Narudzba, napravi_narudzbu

proizvodi = [
    {"naziv": "Laptop", "cijena": 5000, "kolicina": 10},
    {"naziv": "Monitor", "cijena": 1000, "kolicina": 20},
    {"naziv": "Tipkovnica", "cijena": 200, "kolicina": 50},
    {"naziv": "Miš", "cijena": 100, "kolicina": 100}
]

for proizvod in proizvodi:
    dodaj_proizvod(Proizvod(proizvod["naziv"],
                   proizvod["cijena"], proizvod["kolicina"]))


svi_proizvodi = []

for proizvod in proizvodi:
    proizvod_main = Proizvod(
        proizvod["naziv"], proizvod["cijena"], proizvod["kolicina"])
    dodaj_proizvod(proizvod_main)
    svi_proizvodi.append(proizvod_main)

for proizvod in svi_proizvodi:
    proizvod.ispis()

# kreiraj narudzbu
try:
    narudzba = napravi_narudzbu(
        svi_proizvodi,
        [
            {"naziv": "Laptop", "cijena": 500, "kolicina": 1},
            {"naziv": "Monitor", "cijena": 100, "kolicina": 1}
        ]
    )
    rezultat = "Naručeni proizvodi: "
    if narudzba:
        for proizvod in narudzba.proizvodi:
            rezultat += f"{proizvod['naziv']} x {proizvod['kolicina']}, "
        rezultat += f"Ukupna cijena: {narudzba.ukupna_cijena} eur"
        print(rezultat)

except Exception as e:
    print(e)
