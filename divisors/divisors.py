def divisors(n):
    S, T = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            S.append(i)
            T.append(n // i)
        i += 1
    if S[-1] == T[-1]:
        T.pop()
    T.reverse()
    return S + T
