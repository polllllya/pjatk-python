"""
Własny moduł
"""

import math
import sys


def oblic_pole_kola(r):
    return math.pi * r ** 2


def oblicz_obwod_kola(r):
    return math.pi * r * 2


def main():
    print(sys.argv)
    print(oblicz_obwod_kola(int(sys.argv[1])))

if __name__ == "__main__":
    main()

