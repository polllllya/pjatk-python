"""
Modul Random
"""

import random

# from random import * - unikać tego
# from random import randint

random.seed()
print(random.randint(1, 15))
print(random.randint(1, 15))

l = list(range(1, 10))

print(random.choice(l))
print(l)

random.shuffle(l)

print(random.random())  # od 0 do 1

print(random.uniform(10, 30)) #  do 29
