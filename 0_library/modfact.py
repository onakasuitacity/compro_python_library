MOD = 10**9 + 7
class modfact(object):
    def __init__(self, n):
        fact, invfact = [1] * (n + 1), [1] * (n + 1)
        for i in range(1, n + 1): fact[i] = i * fact[i - 1] % MOD
        invfact[n] = pow(fact[n], MOD - 2, MOD)
        for i in range(n - 1, -1, -1): invfact[i] = invfact[i + 1] * (i + 1) % MOD
        self._fact, self._invfact = fact, invfact

    def fact(self, n):
        return self._fact[n]

    def invfact(self, n):
        return self._invfact[n]

    def comb(self, n, k):
        return self._fact[n] * self._invfact[k] % MOD * self._invfact[n - k] % MOD if 0 <= k <= n else 0

    def perm(self, n, k):
        return self._fact[n] * self._invfact[n - k] % MOD if 0 <= k <= n else 0
