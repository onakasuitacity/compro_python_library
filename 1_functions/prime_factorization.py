# prime factorization (O(sqrt(N)))
def prime_factorization(n):
    factor=[]
    sqrt=int(n**.5)
    for d in range(2,sqrt+1):
        while(n%d==0):
            n//=d
            factor.append(d)
    if n!=1: factor.append(n)
    return factor
