"""
Coca-Colę piją obecnie tylko zamożni obywatele. Napisz skrypt,w którym przygotowujesz raport pokazujący zmiany cen tego
popularnego napoju po dodaniu nowego podatku cukrowego:

Ceny przed : 3.69,4.5,3.6,4.0,3.99,3.59
Ceny po : 4.5,5.5,4.69,4.99,4.00

Twoim zadaniem jest podanie informacji o:
a) najwyższej cenie po nałożeniu podatku,
b) najniższej cenie biorąc pod uwagę wszystkie ceny (przed i po),
c) średniej cenie przed podwyżką cen,
d) średniej cenie po dodaniu nowego podatku.
"""

ceny_przed = [3.69, 4.5, 3.6, 4.0, 3.99, 3.59]
ceny_po = [4.5, 5.5, 4.69, 4.99, 4.00]

najwyzsza_cena = ceny_po[0]
najnizsza_cena = ceny_po[0]
sum_przed = 0
sum_po = 0

for i in range(len(ceny_po)):
    if ceny_po[i] > najwyzsza_cena:
        najwyzsza_cena = ceny_po[i]

    if ceny_po[i] < najnizsza_cena:
        najnizsza_cena = ceny_po[i]

    sum_po += ceny_po[i]

for i in range(len(ceny_przed)):
    if ceny_przed[i] < najnizsza_cena:
        najnizsza_cena = ceny_przed[i]

    sum_przed += ceny_przed[i]

srednia_po = sum_po / len(ceny_po)
srednia_przed = sum_przed / len(ceny_przed)

print("Najwyższa cena po nałożeniu podatku:", najwyzsza_cena)
print("Najniższa cena biorąc pod uwagę wszystkie ceny (przed i po):", najnizsza_cena)
print("Średnia cena przed podwyżką cen:", srednia_przed)
print("Średnia cena po dodaniu nowego podatku:", srednia_po)