# https://atcoder.jp/contests/abc138/tasks/abc138_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,q=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        a-=1; b-=1
        E[a].append(b)
        E[b].append(a)

    C=[0]*n
    for _ in range(q):
        p,x=map(int,input().split())
        p-=1
        C[p]+=x

    Q=[(0,-1)]
    while(Q):
        v,p=Q.pop()
        for nv in E[v]:
            if(p==nv): continue
            C[nv]+=C[v]
            Q.append((nv,v))

    print(*C)
resolve()
