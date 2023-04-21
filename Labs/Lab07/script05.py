"""
Dziedziczenie
"""

class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "zwierze"
    zwierzeta = {}

    def __init__(self, gatunek, wiek, predkosc):
        self.gatunek = gatunek
        self.wiek = wiek
        self.max_predkosc = predkosc
        if gatunek in  Zwierz.zwierzeta:
            Zwierz.zwierzeta[gatunek] += 1
        else:
            Zwierz.zwierzeta[gatunek] = 1

    def podaj_gatunek(self):
        print("lis")

    def oblicz_odliglosc(self,czas):
        print(czas  * self.max_predkosc)

    @staticmethod
    def wypisz_zwierzenta():
        print(Zwierz.zwierzeta)


    # Nadpisanie zmiennej specjalnej
    def __str__(self):
        return self.gatunek + " ma " + str(self.wiek) + " lat i osiaga predkosc " + str(self.max_predkosc)+" km/h."

class Ptak(Zwierz):
    def __init__(self,gatunek, wiek, predkosc, max_predkosc_lotu, miejsce):
        super().__init__(gatunek, wiek,predkosc)
        self.predkosc_lotu = max_predkosc_lotu
        self.miejsce = miejsce

    def pprzenies(self):
        if self.miejsce == "klatka":
            self.miejsce = "otwarty"
        else:
            self.miejsce =  "klatka"



a = Ptak("pin",2,3,0,"otwarty")
print(a)

a.pprzenies()
print(a.miejsce)

