"""
Lista B - Lab4 - Zadanie 1
"""

slowo1 = input("Podaj pierwsze słowo: ")
slowo2 = input("Podaj drugie słowo: ")

samogloski = {'a': '7', 'e': '7', 'i': '7', 'o': '7', 'u': '7', 'y': '7'}

spolgloski = {'b': '6', 'c': '6', 'd': '6', 'f': '6', 'g': '6', 'h': '6', 'j': '6', 'k': '6', 'l': '6', 'm': '6', 'n': '6', 'p': '6', 'q': '6', 'r': '6', 's': '6', 't': '6', 'v': '6', 'w': '6', 'x': '6', 'z': '6'}

# zamieniamy samogłoski z pierwszego słowa na liczbę 7
slowo1_zamienione = ''
for litera in slowo1:
    if litera in samogloski:
        slowo1_zamienione += samogloski[litera]
    else:
        slowo1_zamienione += litera

# zamieniamy spółgłoski z drugiego słowa na liczbę 6
slowo2_zamienione = ''
for litera in slowo2:
    if litera in spolgloski:
        slowo2_zamienione += spolgloski[litera]
    else:
        slowo2_zamienione += litera

# łączymy dwa słowa w jedno i zamieniamy wszystkie małe litery na duże
nowe_slowo = ''
for litera in slowo1_zamienione + slowo2_zamienione:
    if litera.islower():
        nowe_slowo += litera.upper()
    else:
        nowe_slowo += litera

print(nowe_slowo)
