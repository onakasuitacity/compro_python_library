# https://atcoder.jp/contests/abc061/tasks/abc061_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    R=[[] for _ in range(n)]
    for _ in range(m):
        a,b,c=map(int,input().split())
        a-=1; b-=1
        E[a].append((b,-c))
        R[b].append((a,-c))

    from collections import deque
    state=[0]*n
    state[0]=1
    state[n-1]=2

    Q=deque([0])
    while(Q):
        v=Q.popleft()
        for nv,w in E[v]:
            if(state[nv]&1): continue
            state[nv]+=1
            Q.append(nv)

    Q=deque([n-1])
    while(Q):
        v=Q.popleft()
        for nv,w in R[v]:
            if(state[nv]&2): continue
            state[nv]+=2
            Q.append(nv)

    dist=[INF]*n
    dist[0]=0
    for k in range(n):
        for v in range(n):
            if(state[v]!=3): continue
            for nv,w in E[v]:
                if(state[nv]!=3): continue
                if(dist[nv]>dist[v]+w):
                    dist[nv]=dist[v]+w
                    if(k==n-1):
                        print("inf")
                        return
    print(-dist[-1])
resolve()
