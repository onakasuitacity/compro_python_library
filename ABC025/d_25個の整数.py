# https://atcoder.jp/contests/abc025/tasks/abc025_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from functools import lru_cache
def resolve():
    G=[x for _ in range(5) for x in map(int,input().split())]
    idx=[None]*26
    for i,x in enumerate(G):
        idx[x]=i

    # S の p bit目を立てて矛盾が起きないか
    def check(S,p):
        if((S>>p)&1): return False
        i,j=p//5,p%5
        if(1<=i<=3):
            u=(S>>(p-5))&1
            d=(S>>(p+5))&1
            if u^d: return False
        if(1<=j<=3):
            l=(S>>(p-1))&1
            r=(S>>(p+1))&1
            if l^r: return False
        return True

    @lru_cache(None)
    def dfs(S,x)->int: # x=popcount(S)+1より不要だが、popcountの定数倍改善
        if(x==26): return 1
        d=idx[x]
        # x が予約されている場合
        if(d is not None):
            return dfs(S^(1<<d),x+1) if(check(S,d)) else 0
        # x が予約されていない場合
        res=0
        for d in range(25):
            if(check(S,d) and (G[d]==0)):
                res+=dfs(S^(1<<d),x+1)
        return res%MOD

    print(dfs(0,1))
resolve()
