# https://atcoder.jp/contests/abc137/tasks/abc137_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
from collections import deque
def resolve():
    n,m,p=map(int,input().split())
    E=[[] for _ in range(n)]
    R=[[] for _ in range(n)]
    edges=[]
    for _ in range(m):
        a,b,c=map(int,input().split())
        a-=1; b-=1
        E[a].append(b)
        R[b].append(a)
        edges.append((a,b,p-c))

    state=[0]*n
    state[0]=1
    state[n-1]=2

    Q=deque([0])
    while(Q):
        v=Q.popleft()
        for nv in E[v]:
            if(state[nv]&1): continue
            state[nv]+=1
            Q.append(nv)

    Q=deque([n-1])
    while(Q):
        v=Q.popleft()
        for nv in R[v]:
            if(state[nv]&2): continue
            state[nv]+=2
            Q.append(nv)

    dist=[INF]*n
    dist[0]=0
    for k in range(n):
        for a,b,w in edges:
            if(state[a]!=3 or state[b]!=3): continue
            if(dist[b]>dist[a]+w):
                dist[b]=dist[a]+w
                if(k==n-1):
                    print(-1)
                    return
    print(max(-dist[-1],0))
resolve()
