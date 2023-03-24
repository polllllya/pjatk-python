def catalan(n):
    if n <= 1:
        return 1
    else:
        result = 0
        for i in range(n):
            result += catalan(i) * catalan(n-i-1)
        return result

max_num = int(input("Podaj górną granicę liczb Catalana: "))
for i in range(max_num):
    c = catalan(i)
    if c < max_num:
        print("{:d}: {:d}".format(i, c))
    else:
        break