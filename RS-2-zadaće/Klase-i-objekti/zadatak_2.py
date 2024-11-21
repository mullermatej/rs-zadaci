class Kalkulator:
    a = 0
    b = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbrajanje(self):
        print(self.a + self.b)

    def oduzimanje(self):
        print(self.a - self.b)

    def mnozenje(self):
        print(self.a * self.b)

    def dijeljenje(self):
        print(self.a / self.b)

    def potenciranje(self):
        print(self.a ** self.b)

    def korijen(self):
        print(f"Korijen od a: {self.a ** .2} i korijen od b: {self.b ** .2}")


argumenti = Kalkulator(4, 2)
argumenti.zbrajanje()
argumenti.oduzimanje()
argumenti.mnozenje()
argumenti.dijeljenje()
argumenti.potenciranje()
argumenti.korijen()
