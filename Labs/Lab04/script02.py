"""
Lab04 - Instrukcje  warunkowe
"""

# Przykłady prostych instrukcji warunkowych
if 1 < 2:
    print("Prawda")

if True:
    print("Prawda")

if "napis":
    print("Prawda")

if 1:
    print("Prawda")

if None:
    print("Prawda")

x = True
y = False

if x and y:
    print("prawda")

print()
# Zagnieżdżone instr. warunkowe
a = -1
if a < 0:
    print("Czerwony")
    if a != 20:
        print("Bingo" * 3)

print()

# Bardziej rozbudowane
wybor = int(input("Podaj dowolną liczbę całkowitą: "))
if wybor < 0:
    print("Czerwony")
elif wybor == 0:
    print("Biały")
else:
    print("Zielony")

print()

if wybor < 0:
    print("Czerwony")
else:
    print("Zelony")

print()

if 10 <= wybor <= 100:
    print("<10-100>")
else:
    print("Zły zakres")

print()

