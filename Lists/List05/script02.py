"""
Napisz funkcję wypisującą liczby Catalana.
Zmodyfikuj kod z zadania wykonanego na jednych z poprzenich zajęć.
Funkcja powinna umożliwić użytkownikowi wyświetlenie liczb Catalana parzystych, nieparzystych lub wszyskichmniejszych od liczby podanej w argumnecie.
Domyślnie funkcja wyświetla wszystkie liczby.
funckja (N, {p,n,a})
"""


def catalan_numbers(N, options={'p': False, 'n': False, 'a': True}):
    cat_nums = [1]
    for n in range(1, N):
        cat_num = 0
        for i in range(n):
            cat_num += cat_nums[i] * cat_nums[n - i - 1]
        cat_nums.append(cat_num)

    if options['p']:
        cat_nums = [num for num in cat_nums if num % 2 == 0]
    elif options['n']:
        cat_nums = [num for num in cat_nums if num % 2 != 0]

    for num in cat_nums:
        if num > N:
            break
        print(num)


catalan_numbers(20, options={'p': True})
catalan_numbers(20, options={'n': True})
catalan_numbers(20)
