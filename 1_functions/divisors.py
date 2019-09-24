# divisors (O(sqrt(N)))
def divisors(n):
    S,T=[],[]
    for i in range(1,int(n**.5)+1):
        if n%i==0:
            S.append(i)
            T.append(n//i)
    T.reverse()
    return S+T if S[-1]!=T[0] else S+T[1:]
