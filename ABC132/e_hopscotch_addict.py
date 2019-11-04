# https://atcoder.jp/contests/abc132/tasks/abc132_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(3*n)]
    for _ in range(m):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[3*u].append(3*v+1)
        E[3*u+1].append(3*v+2)
        E[3*u+2].append(3*v)
    s,t=map(int,input().split())
    s-=1; t-=1

    # BFS (startは0、goalは3n-3)
    from collections import deque
    d=[-1]*(3*n)
    d[3*s]=0
    Q=deque()
    Q.append(3*s)
    while(Q):
        v=Q.popleft()
        for nv in E[v]:
            if(d[nv]!=-1): continue
            d[nv]=d[v]+1
            Q.append(nv)
    ans=d[3*t]
    print(ans//3 if(ans!=-1) else -1)
resolve()
