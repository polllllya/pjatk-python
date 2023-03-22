"""
Lab03 - Krotki
"""

# nie modyfikowalne!
# tuple(eng)
# działa szybciej niż listta

# tworzenie
krotka1 = 1,
print(krotka1)

krotka1 = (1,)
print(krotka1)

krotka2 = 1, 3.14, "cos"
print(krotka2)

krotka3 = 1, 3.14, [1, 2]
print(krotka3)

napis = "adad"
print(tuple(napis))

# Indeksowanoe
print(krotka2[0])
print(krotka2[:2])

# Operacje na krotkach
x = 1, 2, 3, 1
# liczy ilosc
print(x.count(1))
#zwraca index pierwszego elementu
print(x.index(1))


