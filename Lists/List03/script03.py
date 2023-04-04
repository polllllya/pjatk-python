import random

# Kolekcja kategorii i słów do odgadnięcia
slowa = {
    "owoce": ["jabłko", "banan", "gruszka", "cytryna", "truskawka"],
    "kraje": ["polska", "niemcy", "francja", "włochy", "białoruś"],
    "kolory": ["czerwony", "zielony", "niebieski", "żółty", "fioletowy"]
}

# Wybór kategorii i słowa do odgadnięcia
kategorie = list(slowa.keys())
wybrana_kategoria = random.choice(kategorie)
slowa_w_kategorii = slowa[wybrana_kategoria]
wybrane_slowo = random.choice(slowa_w_kategorii)


gracz1_pkt = 0
gracz2_pkt = 0
odkryte_litery = set()

# Funkcja sprawdzająca, czy litera znajduje się w słowie do odgadnięcia
def sprawdz_litere(litera):
    if litera in wybrane_slowo:
        odkryte_litery.add(litera)
        return True
    return False

# Pętla gry
while True:
    # Wyświetlenie kategorii i znaków podkreślenia zamiast liter
    print("Kategoria:", wybrana_kategoria)
    for litera in wybrane_slowo:
        if litera in odkryte_litery:
            print(litera, end=" ")
        else:
            print("_", end=" ")
    print()

    # Gracz 1 podaje literę
    litera = input("Gracz 1 - podaj literę: ").lower()
    if sprawdz_litere(litera):
        print("Dobra odpowiedź!")
        gracz1_pkt += wybrane_slowo.count(litera)
    else:
        print("Błędna odpowiedź.")
        # Gracz 2 dostaje szansę
        litera = input("Gracz 2 - podaj literę: ").lower()
        if sprawdz_litere(litera):
            print("Dobra odpowiedź!")
            gracz2_pkt += wybrane_slowo.count(litera)
        else:
            print("Błędna odpowiedź.")

    # Sprawdzenie, czy zostało odgadnięte całe słowo
    if set(wybrane_slowo) == odkryte_litery:
        # Obliczenie punktów za nieodkryte litery
        nieodkryte_litery = set(wybrane_slowo) - odkryte_litery
        punkty = len(nieodkryte_litery) * 2
        gracz1_pkt += punkty

        print("#############################")
        print("Punkty:")
        print("Gracz 1:", gracz1_pkt)
        print("Gracz 2:", gracz2_pkt)
        break