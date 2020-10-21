from collections import Counter
def prime_factorization(n):
    factor = Counter()
    for p in range(2, int(n**.5) + 1):
        while n % p == 0:
            n //= p
            factor[p] += 1
    if n != 1:
        factor[n] += 1
    return factor
