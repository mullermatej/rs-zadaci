import datetime


class Automobil:
    marka = ""
    model = ""
    godina_proizvodnje = 0
    kilometraza = 0

    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(self.marka)
        print(self.model)
        print(self.godina_proizvodnje)
        print(self.kilometraza)

    def starost(self):
        vrijeme = datetime.date.today()
        starost_auta = vrijeme.year - self.godina_proizvodnje
        print(f"Automobil je star {starost_auta} godine")


auto = Automobil("BMW", "440i", 2020, 50000)
auto.ispis()
auto.starost()
