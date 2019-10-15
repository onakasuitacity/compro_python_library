# https://atcoder.jp/contests/abc138/tasks/abc138_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
input=lambda :sys.stdin.buffer.readline().rstrip()
class ModInt(object):
    __MOD=10**9+7

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
    from itertools import product
    L,R=map(int,input().split())
    D=R.bit_length()
    dp=[[[[ModInt(0)]*2 for _ in range(2)] for _ in range(2)] for _ in range(D+1)]
    dp[D][0][0][0]=ModInt(1)
    for d in range(D-1,-1,-1):
        lb=L>>d&1; rb=R>>d&1
        for i,j,m,x,y in product([0,1],repeat=5):
            ni,nj,nm=i,j,m
            if(x>y): continue
            # i:L<=X
            if(i==0 and lb>x): continue
            if(lb<x): ni=1
            # j:Y<=R
            if(j==0 and y>rb): continue
            if(y<rb): nj=1
            # m:MSB
            if(m==0 and x!=y): continue
            if(x==1 and y==1): nm=1
            dp[d][ni][nj][nm]+=dp[d+1][i][j][m];
    print(sum(dp[0][i][j][m] for i,j,m in product([0,1],repeat=3)))
resolve()
