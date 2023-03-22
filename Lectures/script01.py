persons = [("Ann", 23), ("Bea", 45), ("Sue", 13)]
for name, age in persons:
    print('{} is {} years old'.format(name, age))

it = persons.__iter__()  # or it = iter(persons)

a = it.__next__()
print('{} is {} years old'.format(a[0], a[1]))

print()

lst = [1, 7, 4, 9, 2, 6, 3]
indsOdd = []
for i, e in enumerate(lst):
    if e % 2 != 0:
        indsOdd += [i]
print('Odd elements at positions', indsOdd)

print()

seasons = ["Spring", "Summer", "Autumn", "Winter"]
for ind, s in enumerate(seasons, 1):
    print('Season', ind, '->', s)

print()

r = range(1, 6, 2)
print(type(r))
print(r)
print(len(r))

print()

k = 3
match k:
    case 0:
        print('zero')
    case 1 | 2 | 3 | 4:
        print('less than 5')
    case 5:
        print('five')
    case _:
        raise ValueError()
    


#kontynuacja
print("shdjfkfejhfejfef\
      dnvhbdhhv")

