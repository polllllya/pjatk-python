class Produkt:
    kategorie = {"warzywo i owoce": [], "produkt mleczny": [], "mieso": []}
    FILENAME = "produkty.txt"

    def __init__(self, nazwa, cena, kategoria):
        self.cena = cena
        self.nazwa = nazwa
        self.kategoria = kategoria

        if kategoria == "warzywo i owoce":
            Produkt.kategorie["warzywo i owoce"].append(self)
        if kategoria == "produkt mleczny":
            Produkt.kategorie["produkt mleczny"].append(self)
        if kategoria == "mieso":
            Produkt.kategorie["mieso"].append(self)

    def oblicz_calkowity_koszt(self, ilosc):
        print("Całkowity koszt:", self._oblicz_znizke() * ilosc)

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
        return f"{self.nazwa} kosztuje {self.cena} i należy do kategorii {self.kategoria}"

    @staticmethod
    def zapisz_do_pliku():
        try:
            with open(Produkt.FILENAME, "w") as file:
                for kategoria, produkty in Produkt.kategorie.items():
                    for produkt in produkty:
                        file.write(f"{produkt.nazwa},{produkt.cena},{produkt.kategoria}\n")
        except IOError:
            print("Błąd podczas zapisu do pliku")

    @staticmethod
    def odczytaj_z_pliku():
        try:
            with open(Produkt.FILENAME, "r") as file:
                lines = file.readlines()
                for line in lines:
                    nazwa, cena, kategoria = line.strip().split(",")
                    Produkt(nazwa, float(cena), kategoria)
        except IOError:
            print("Błąd podczas odczytu z pliku")

p1 = Produkt("Mleko", 2.34, "produkt mleczny")
p2 = Produkt("Kurczak", 8.32, "mieso")
p3 = Produkt("Banan", 2.60, "warzywo i owoce")
p4 = Produkt("Ziemniak", 0.30, "warzywo i owoce")
p5 = Produkt("Smietana", 4.68, "produkt mleczny")

Produkt.wypisz_produkt()

p1.oblicz_calkowity_koszt(4)

print(p2)

Produkt.zapisz_do_pliku()

Produkt.odczytaj_z_pliku()
