# Eratosthenes Sieve (O(nloglogn))
def primes(n):
    if n <= 1: return []
    S = [1] * (n + 1)
    S[0] = S[1] = 0
    for i in range(2, n):
        if S[i] == 0: continue
        for j in range(2 * i, n + 1, i): S[j] = 0
    return [p for p in range(n + 1) if(S[p])]
