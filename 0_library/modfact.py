MOD = 10**9 + 7
class modfact(object):
    def __init__(self, n):
        fact, invfact = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1): fact[i] = i * fact[i - 1] % MOD
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1): invfact[i] = invfact[i + 1] * (i + 1) % MOD
        self.fact, self.invfact = fact, invfact

    def inv(self, n):
        return self.fact[n-1] * self.invfact[n] % MOD

    def fact(self, n):
        return self.fact[n]

    def invfact(self,n):
        return self.invfact[n]

    def comb(self,n,k):
        if k < 0 or n < k: return 0
        return self.fact[n] * self.invfact[k] % MOD * self.invfact[n - k] % MOD

    def perm(self,n,k):
        if k < 0 or n < k: return 0
        return self.fact[n] * self.invfact[n - k] % MOD
