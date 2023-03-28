"""
Lista B - Lab3 - Zadanie 3
"""

# pobieranie danych od użytkownika
litery = input("Podaj duże litery alfabetu, oddzielone przecinkami: ").split(",")
liczby = input("Podaj liczby od 1 do 10, oddzielone przecinkami: ").split(",")

# tworzenie słownika
slownik = {litery[i]: liczby[i] for i in range(len(litery))}

# wyświetlanie słownika
print(slownik)