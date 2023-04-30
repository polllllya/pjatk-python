"""
Użycie własnego modólu
"""

import funkcje
from funkcje import oblicz_obwod_kola

obwod = oblicz_obwod_kola(4)

print(obwod)

# Pakiety
import prz_pakiet.funkcje as f

pole = f.oblic_pole_kola(5)
print(pole)