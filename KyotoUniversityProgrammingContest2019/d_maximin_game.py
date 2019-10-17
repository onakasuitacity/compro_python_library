# https://atcoder.jp/contests/kupc2019/tasks/kupc2019_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
input=lambda :sys.stdin.buffer.readline().rstrip()
class ModInt(object):
    __MOD=998244353

    def __init__(self,x):
        self.__x=x%self.__MOD

    def __repr__(self):
        return str(self.__x)

    def __add__(self,other):
        return ModInt(self.__x+other.__x) if isinstance(other,ModInt) else ModInt(self.__x+other)

    def __sub__(self,other):
        return ModInt(self.__x-other.__x) if isinstance(other,ModInt) else ModInt(self.__x-other)

    def __mul__(self,other):
        return ModInt(self.__x*other.__x) if isinstance(other,ModInt) else ModInt(self.__x*other)

    def __truediv__(self,other):
        return ModInt(self.__x*pow(other.__x,self.__MOD-2,self.__MOD)) if isinstance(other, ModInt) else ModInt(self.__x*pow(other, self.__MOD-2,self.__MOD))

    def __pow__(self,other):
        return ModInt(pow(self.__x,other.__x,self.__MOD)) if isinstance(other,ModInt) else ModInt(pow(self.__x,other,self.__MOD))

    __radd__=__add__

    def __rsub__(self,other):
        return ModInt(other.__x-self.__x) if isinstance(other,ModInt) else ModInt(other-self.__x)

    __rmul__=__mul__

    def __rtruediv__(self,other):
        return ModInt(other.__x*pow(self.__x,self.__MOD-2,self.__MOD)) if isinstance(other,ModInt) else ModInt(other*pow(self.__x,self.__MOD-2,self.__MOD))

    def __rpow__(self,other):
        return ModInt(pow(other.__x,self.__x,self.__MOD)) if isinstance(other,ModInt) else ModInt(pow(other,self.__x,self.__MOD))

def resolve():
    from math import factorial
    from itertools import groupby
    ans=ModInt(1)
    n=int(input())
    s=input()
    G=groupby(s)
    for key,it in G:
        k=len(list(it))
        ans*=factorial(2*k)
        ans/=(factorial(k)*factorial(k)*(k+1))
    print(ans)
resolve()
