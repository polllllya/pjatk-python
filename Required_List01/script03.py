"""
Napisz skrypt rysujący z gwiazdek * prostokąt o długości a=3 i szerokości b=4.
Spraw aby skrypt obliczał i wyświetlał pole oraz obwód tego prostokąta.
"""

a = 3
b = 4

pole = a * b
obwod = 2 * (a + b)

for i in range(a):
    for j in range(b):
        if i == 0 or j == 0 or i == a - 1 or j == b - 1:
            print("* ", end="")
        else:
            print("  ", end="")
    print()

print("Pole:", pole, "\nOdwod:", obwod)