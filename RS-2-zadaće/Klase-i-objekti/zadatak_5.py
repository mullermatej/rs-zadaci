class Radnik:
    ime = ""
    pozicija = ""
    placa = 0

    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}")
        return


class Menadzer(Radnik):
    department = ""

    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}")
        return

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje


radnik = Radnik("Ivo", "Programer", 1000)
menadzer = Menadzer("Ana", "Menadzer", 2000, "HR")

radnik.work()
menadzer.work()
menadzer.give_raise(radnik, 300)
