# divisors (O(sqrt(N)))
def divisors(n):
    S, T = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            S.append(i)
            T.append(n // i)
        i += 1
    T.reverse()
    return S + T if S[-1] != T[0] else S + T[1:]
