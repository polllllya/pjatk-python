'''
Lab06 - Zakres zmiennych
'''

print("Zakrees lokalny")
x = 5


def show(a):
    x = a
    print(x)


show(2)
print(x)

y  = 7
def show2(b):
    global y
    y = b
    print(y)

show(2)
print(y)

