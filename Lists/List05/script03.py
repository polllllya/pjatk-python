"""
Napisz generator liczb pierwszych uzyskanych metodą sita Eratostenesa.
Domyślnie generator wyświetla pierwszych100liczb pierwszych.
"""


def primes_sieve(n=541):
    sieve = [True] * (n + 1)
    sieve[0], sieve[1] = False, False
    for i in range(2, n + 1):
        if sieve[i]:
            yield i
            for j in range(i * i, n + 1, i):
                sieve[j] = False


primes = primes_sieve()
for i in range(50):
    print(next(primes))
