def crible_eratosthene(n):
    primes = [1] * (n + 1)
    for i in range(2, int(n**0.5) + 1):
        if primes[i] == 1:
            for j in range(i*i, n+1, i):
                primes[j] = 0
    prime_numbers = [index for index, value in enumerate(primes) if value == 1][2:]
    return prime_numbers
result = crible_eratosthene(1000)

print(result)
