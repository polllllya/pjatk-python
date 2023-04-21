"""
Napisz skrypt tworzący słownik, którego kluczami będą nicki z zadania 1,a wartościami liczba pkt.
"""

slownik = {"LeBron James": 10.6, "Kevin Durant": 9.1, "Stephen Curry": 7.4, "Giannis Antetokounmpo": 6.6,
           "James Harden": 6.3}

for key, value in slownik.items():
    print(key, "-", end=" ")
    print(value)