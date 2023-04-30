"""
Napisz skrypt, który będzie działał jak prosta baza produktów spożywczych.
Skrypt ma korzytać z klas.Zmodyfikuj kod z zadania wykonanego na jednych z poprzednich zajęć.
"""


class Produkt:
    kategorie = {"warzywo i owoce": [], "produkt mleczny": [], "mieso": []}

    def __init__(self, nazwa, cena, kategorja):
        self.cena = cena
        self.nazwa = nazwa
        self.kategorja = kategorja

        if kategorja == "warzywo i owoce":
            Produkt.kategorie["warzywo i owoce"].append(self)
        if kategorja == "produkt mleczny":
            Produkt.kategorie["produkt mleczny"].append(self)
        if kategorja == "mieso":
            Produkt.kategorie["mieso"].append(self)

    def oblicz_calkowity_koszt(self, ilosc):
        print("Calkowity koszt:", self._oblicz_znizke() * ilosc)

    def _oblicz_znizke(self):
        return self.cena - (self.cena * 10 / 100)

    @staticmethod
    def wypisz_produkt():
        print("Produkty:")
        for kategoria, produkty in Produkt.kategorie.items():
            print(f"Kategoria: {kategoria}")
            for produkt in produkty:
                print(f"Nazwa: {produkt.nazwa}, Cena: {produkt.cena}")
            print()


    def __str__(self):
        return f"{self.nazwa} kosztuje {self.cena} i należy do kategorii {self.kategorja}"


p1 = Produkt("Mleko", 2.34, "produkt mleczny")
p2 = Produkt("Kurczak", 8.32, "mieso")
p3 = Produkt("Banan", 2.60, "warzywo i owoce")
p4 = Produkt("Ziemniak", 0.30, "warzywo i owoce")
p5 = Produkt("Smietana", 4.68, "produkt mleczny")

Produkt.wypisz_produkt()

p1.oblicz_calkowity_koszt(4)
print(p2)