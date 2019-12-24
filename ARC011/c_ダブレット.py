# https://atcoder.jp/contests/arc011/tasks/arc011_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from collections import deque
def resolve():
    first,last=input().split()

    if(first==last):
        print(0)
        print(first)
        print(last)
        return

    n=int(input())
    S=[first]+[input() for _ in range(n)]+[last]
    n+=2

    # 各頂点に辺を張っていく
    E=[[] for _ in range(n)]
    for j in range(n):
        for i in range(j):
            d=sum(s!=t for s,t in zip(S[i],S[j]))
            if(d>1): continue
            E[i].append((j,d))
            E[j].append((i,d))

    # 0 から n-1 への最短経路を求める
    Q=deque([0])
    dist=[INF]*n
    dist[0]=0
    prev=[None]*n
    while(Q):
        v=Q.popleft()
        for nv,w in E[v]:
            if(dist[nv]>dist[v]+w):
                dist[nv]=dist[v]+w
                prev[nv]=v
                Q.appendleft(nv) if(w==0) else Q.append(nv)

    if(dist[-1]==INF):
        print(-1)
        return

    # path restoration
    print(dist[-1]-1)
    now=n-1
    path=[]
    while(now is not None):
        path.append(S[now])
        now=prev[now]
    path.reverse()
    print(*path,sep='\n')
resolve()
