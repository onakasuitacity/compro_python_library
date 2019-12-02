# https://atcoder.jp/contests/abc025/tasks/abc025_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from functools import lru_cache
from itertools import chain
def resolve():
    B=[tuple(map(int,input().split())) for _ in range(2)]
    C=[tuple(map(int,input().split())) for _ in range(3)]

    @lru_cache(None)
    def dfs(A):
        if(A.count(None)==0):
            res=0
            res+=sum(b for i,b in zip(range(6),chain.from_iterable(B)) if(A[i]==A[i+3]))
            res+=sum(c for i,c in zip((0,1,3,4,6,7),chain.from_iterable(C)) if(A[i]==A[i+1]))
            return res

        turn=9-A.count(None)
        if(turn&1==0):
            res=-INF
            for i in range(9):
                if(A[i] is None):
                    X=list(A)
                    X[i]=0
                    res=max(res,dfs(tuple(X)))
            return res
        else:
            res=INF
            for i in range(9):
                if(A[i] is None):
                    X=list(A)
                    X[i]=1
                    res=min(res,dfs(tuple(X)))
            return res

    s=sum(chain.from_iterable(B))+sum(chain.from_iterable(C))
    ans=dfs(tuple([None]*9))
    print(ans)
    print(s-ans)
resolve()
