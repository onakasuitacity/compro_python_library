# https://atcoder.jp/contests/abc036/tasks/abc036_d
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
    n=int(input())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(lambda x:int(x)-1,input().split())
        E[a].append(b)
        E[b].append(a)
    dp=[[ModInt(1)]*2 for _ in range(n)] # 別に1で初期化する必要なさそう
    # dfs
    def dfs(v,p):
        white=black=ModInt(1)
        for nv in E[v]:
            if(nv==p): continue
            dfs(nv,v)
            white*=dp[nv][0]+dp[nv][1]
            black*=dp[nv][0]
        dp[v][0]=white
        dp[v][1]=black
    # output
    dfs(0,-1)
    print(dp[0][0]+dp[0][1])
resolve()
