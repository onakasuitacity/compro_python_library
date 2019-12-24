# https://atcoder.jp/contests/arc056/tasks/arc056_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from heapq import heappop,heappush
def resolve():
    n,m,s=map(int,input().split())
    s-=1
    E=[[] for _ in range(n)]
    for _ in range(m):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[u].append(v)
        E[v].append(u)

    # dp[v] : s から v に到達するのに経由する必要のある頂点のうち最小のもの
    dp=[-INF]*n
    dp[s]=s
    Q=[(-s,s)] # 値の大きいものから取り出す(昇順のためマイナスにしている)
    while(Q):
        c,v=heappop(Q)
        c=-c
        if(dp[v]>c): continue
        for nv in E[v]:
            if(dp[nv]<min(nv,c)):
                dp[nv]=min(nv,c)
                heappush(Q,(-min(nv,c),nv))

    for v in range(n):
        if(v==dp[v]):
            print(v+1)
resolve()
