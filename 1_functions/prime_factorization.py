# prime factorization (O(sqrt(N)))
def trial_division(n):
    factor=[]
    sqrt=int(n**.5)+1 # sqrt=ceil(sqrt(n))
    for d in range(2,sqrt):
        while(n%d==0):
            n//=d
            factor.append(d)
    if n==1: return factor
    else: return factor+[n]
