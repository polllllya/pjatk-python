"""
Polimorfizm. Metody prywatne
"""


class Zwierz:
    """Pierwsza klasa"""
    rodzaj = "zwierze"
    zwierzeta = {}

    def __init__(self, gatunek, wiek, predkosc, stan_zdrowia):
        self.gatunek = gatunek
        self.wiek = wiek
        self.stan_drowia = stan_zdrowia
        self.max_predkosc = predkosc
        if gatunek in Zwierz.zwierzeta:
            Zwierz.zwierzeta[gatunek] += 1
        else:
            Zwierz.zwierzeta[gatunek] = 1

    def podaj_gatunek(self):
        print("lis")

    def oblicz_odliglosc(self, czas):
        print(czas * self.max_predkosc)


    def _sprawdz_stan_zdrowia(self):
        if self.stan_drowia == 1:
            return 1
        else:
            return 0

    @staticmethod
    def wypisz_zwierzenta():
        print(Zwierz.zwierzeta)

    # Nadpisanie zmiennej specjalnej
    def __str__(self):
        return self.gatunek + " ma " + str(self.wiek) + " lat i osiaga predkosc " + str(self.max_predkosc) + " km/h."


class Ptak(Zwierz):
    def __init__(self, gatunek, wiek, predkosc,stan_zdrowia, max_predkosc_lotu, miejsce):
        super().__init__(gatunek, wiek, predkosc, stan_zdrowia)
        self.predkosc_lotu = max_predkosc_lotu
        self.miejsce = miejsce

    def pprzenies(self):
        if self.miejsce == "klatka" and self._sprawdz_stan_zdrowia() == 1:
            self.miejsce = "otwarty"
        else:
            self.miejsce = "klatka"


    def oblicz_odliglosc(self, czas):
        if self.predkosc_lotu == 0:
            print(czas * self.max_predkosc)
        else:
            print(czas * self.predkosc_lotu)

p = Ptak("pingwin", 2, 3, 1, 0, "otwarty")
p1 = Ptak("kos", 2, 2, 1, 15, "klatka")

p.oblicz_odliglosc(2)
p1.oblicz_odliglosc(2)

# Metody prywatne
p.pprzenies()
print(p.miejsce)

p1.pprzenies()
print(p1.miejsce)