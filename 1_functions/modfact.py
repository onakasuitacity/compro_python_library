MOD=10**9+7
class modfact(object):
    def __init__(self,n):
        fact=[1]*(n+1)
        invfact=[1]*(n+1)
        for i in range(1,n+1):
            fact[i]=i*fact[i-1]%MOD
        invfact[n]=pow(fact[n],MOD-2,MOD)
        for i in range(n-1,-1,-1):
            invfact[i]=invfact[i+1]*(i+1)%MOD
        self.__fact=fact
        self.__invfact=invfact

    def fact(self,n):
        return self.__fact[n]

    def invfact(self,n):
        return self.__invfact[n]

    def comb(self,n,k):
        if(k<0 or n-k<0): return 0
        return (self.fact(n)*self.invfact(k)*self.invfact(n-k))%MOD
