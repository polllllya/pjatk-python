"""
Lista B - Lab3 - Zadanie 1
"""

# pobieranie danych od użytkownika
imie = input("Podaj swoje imię: ")
data_urodzenia = input("Podaj swoją datę urodzenia (w formacie RRRR-MM-DD): ")
email = input("Podaj swój adres e-mail: ")
numer_telefonu = input("Podaj swój numer telefonu: ")

# zapisywanie danych w postaci listy, krotki i słownika
dane_lista = [imie, data_urodzenia, email, numer_telefonu]
dane_krotka = (imie, data_urodzenia, email, numer_telefonu)
dane_slownik = {"imie": imie, "data_urodzenia": data_urodzenia, "email": email, "numer_telefonu": numer_telefonu}

# wyświetlanie danych na ekranie
print("Twoje dane w postaci listy:")
print(dane_lista)

print("\nTwoje dane w postaci krotki:")
print(dane_krotka)

print("\nTwoje dane w postaci słownika:")
print(dane_slownik)