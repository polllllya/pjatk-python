'''
Lab06 - Lambda
'''

l = lambda a, b, c: a + b + c
print(l(2, 3, 4))

list = [(lambda a: a * 2), (lambda a: a * 4)]

for el in list:
    print(el(2))

print(list[1](3))
