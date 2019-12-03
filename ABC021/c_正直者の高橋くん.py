# https://atcoder.jp/contests/abc021/tasks/abc021_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    E=[[] for _ in range(n)]
    a,b=map(int,input().split())
    a-=1; b-=1
    for _ in range(int(input())):
        x,y=map(int,input().split())
        x-=1; y-=1
        E[x].append(y)
        E[y].append(x)

    from collections import deque
    dist=[INF]*n
    dist[b]=0
    dp=[0]*n
    dp[b]=1
    Q=deque([b])
    while(Q):
        v=Q.popleft()
        for nv in E[v]:
            if(dist[nv]>dist[v]+1):
                dist[nv]=dist[v]+1
                dp[nv]+=dp[v]
                dp[nv]%=MOD
                Q.append(nv)
            elif(dist[nv]==dist[v]+1):
                dp[nv]+=dp[v]
                dp[nv]%=MOD

    print(dp[a])
resolve()
