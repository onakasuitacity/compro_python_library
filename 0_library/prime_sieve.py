def prime_sieve(N):
    primes = []
    sieve = list(range(N + 1))
    for i in range(2, N + 1):
        if sieve[i] == i:
            primes.append(i)
        for p in primes:
            if sieve[i] < p or i * p > N:
                break
            sieve[i * p] = p
    return primes, sieve
