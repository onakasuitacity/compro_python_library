MOD=10**9+7
def modfact(n):
    fact=[1]*(n+1)
    invfact=[1]*(n+1)
    for i in range(1,n+1):
        fact[i]=i*fact[i-1]%MOD
    invfact[n]=pow(fact[n],MOD-2,MOD)
    for i in range(n-1,-1,-1):
        invfact[i]=invfact[i+1]*(i+1)%MOD
    return fact,invfact
