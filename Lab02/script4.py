'''
Lab02 - operacje na lancuchach i konwersja tupów
'''

napis = "Wiek:  " + str(10)
print(napis)

# Zmianaznaków w tekscie
print(napis.replace("W", "w"))

print(napis.upper())
print(napis.lower())

# konwersja typu tekstowego na tym liczbowy
a = "5"
b = 7
print(int(a) + b)

# konwersja typu liczbowego na tym tekstowy
a = "6"
b = 7
print(a + repr(b))
print(a + str(b))

