"""
Lab04 - słowniki
"""

# Tworzenie słownika

# {} - również zbiór
s = {}
print(s)

s = dict()
print(s)

s = {"Nazwisko": "Rolf", "Wiek": "25"}
print(s)

s = dict([("Nazwisko", "Wolf"), ("Wiek", "25")])
print(s)

s = dict(Nazwisko="Wolf", Wiek="25")
print(s)

# operacje na słownikach
nazwisko = s["Nazwisko"]
print(nazwisko)

wiek = s.get("Wiek")
print(wiek)

s["Nazwisko"] = "Blue"
print(s)

nowe_elem = {"Zawód": "Informatyk", "Klasa": 1}
s.update(nowe_elem)
print(s)

s.pop("Zawód")
print(s)

del s["Klasa"]
print(s)

# Wybrane metody
print(s.keys())
print(s.values())

# Zwraca krotki
print(s.items())

