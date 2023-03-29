"""
Lab03 - Zbiory
"""

# może mieć tylko unikalne wartości

# Tworzenie
zb1 = {}
print(zb1)

zb1 = {1, 2, 3}
print(zb1)

print(zb1.pop())
print(zb1)

zb2 = set((3, 5, 7, 2))

# operacje na zbiorach
print(zb1.union(zb2))
print(zb1 | zb2)

print(zb1.intersection(zb2))
print(zb1 & zb2)

print(zb1 - zb2)
print(zb1.difference(zb2))

print(zb2 - zb1)
print(zb2.difference(zb1))

print(zb1.symmetric_difference(zb1))
print(zb1 ^ zb2)

zb3 = {1, 4, 5, 8.7}
zb3.remove(8.7)

zb3 = {1, 4, 5, 8.7}
zb3.discard(8.7)

zb3.clear()
print(zb3)

