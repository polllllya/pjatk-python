import tkinter as tk

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

def wypisz_produkty():
    text_area.delete("1.0", tk.END)
    for kategoria, produkty in Produkt.kategorie.items():
        text_area.insert(tk.END, f"Kategoria: {kategoria}\n")
        for produkt in produkty:
            text_area.insert(tk.END, f"Nazwa: {produkt.nazwa}, Cena: {produkt.cena}\n")
        text_area.insert(tk.END, "\n")

def dodaj_produkt():
    nazwa = entry_nazwa.get()
    cena = float(entry_cena.get())
    kategoria = dropdown_kategoria.get()
    Produkt(nazwa, cena, kategoria)
    wypisz_produkty()

root = tk.Tk()
root.title("Prosta baza produktów spożywczych")

label_nazwa = tk.Label(root, text="Nazwa:")
label_nazwa.grid(row=0, column=0, padx=10, pady=10)
label_cena = tk.Label(root, text="Cena:")
label_cena.grid(row=1, column=0, padx=10, pady=10)
label_kategoria = tk.Label(root, text="Kategoria:")
label_kategoria.grid(row=2, column=0, padx=10, pady=10)
label_ilosc = tk.Label(root, text="Ilość:")
label_ilosc.grid(row=3, column=0, padx=10, pady=10)

entry_nazwa = tk.Entry(root)
entry_nazwa.grid(row=0, column=1, padx=10, pady=10)
entry_cena = tk.Entry(root)
entry_cena.grid(row=1, column=1, padx=10, pady=10)
entry_ilosc = tk.Entry(root)
entry_ilosc.grid(row=3, column=1, padx=10, pady=10)

button_dodaj = tk.Button(root, text="Dodaj produkt", command=dodaj_produkt)
button_dodaj.grid(row=4, column=0, padx=10, pady=10)
button_wypisz = tk.Button(root, text="Wypisz produkty", command=wypisz_produkty)
button_wypisz.grid(row=4, column=1, padx=10, pady=10)

kategorie = list(Produkt.kategorie.keys())
dropdown_kategoria = tk.StringVar(root)
dropdown_kategoria.set(kategorie[0])
dropdown_kategorie = tk.OptionMenu(root, dropdown_kategoria, *kategorie)
dropdown_kategorie.grid(row=2, column=1, padx=10, pady=10)

text_area = tk.Text(root, height=10, width=50)
text_area.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
