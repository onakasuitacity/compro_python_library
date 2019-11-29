# https://atcoder.jp/contests/abc049/tasks/arc065_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from itertools import groupby
def resolve():
    n,k,l=map(int,input().split())
    K=[[] for _ in range(n)]
    L=[[] for _ in range(n)]
    for _ in range(k):
        p,q=map(int,input().split())
        p-=1; q-=1
        K[p].append(q)
        K[q].append(p)
    for _ in range(l):
        r,s=map(int,input().split())
        r-=1; s-=1
        L[r].append(s)
        L[s].append(r)

    # KについてのDFS
    C1=[-1]*n
    col=0
    def dfs1(v)->bool:
        if(C1[v]!=-1): return False
        C1[v]=col
        Q=[v]
        while(Q):
            v=Q.pop()
            for nv in K[v]:
                if(C1[nv]!=-1): continue
                C1[nv]=col
                Q.append(nv)
        return True

    for v in range(n):
        col+=dfs1(v)

    # LについてのDFS
    C2=[-1]*n
    col=0
    def dfs2(v)->bool:
        if(C2[v]!=-1): return False
        C2[v]=col
        Q=[v]
        while(Q):
            v=Q.pop()
            for nv in L[v]:
                if(C2[nv]!=-1): continue
                C2[nv]=col
                Q.append(nv)
        return True

    for v in range(n):
        col+=dfs2(v)

    ans=[None]*n
    X=[(C1[v],C2[v],v) for v in range(n)]
    X.sort()
    for key,iter in groupby(X,key=lambda x:(x[0],x[1])):
        s=list(iter)
        for a,b,c in s:
            ans[c]=len(s)
    print(*ans)
resolve()
