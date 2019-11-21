# https://atcoder.jp/contests/abc077/tasks/arc084_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()

from collections import deque
def resolve():
    k=int(input())
    E=[[] for _ in range(k)]
    for i in range(k):
        E[i].append(((i+1)%k,1))
        E[i].append(((10*i)%k,0))

    # 0-1 BFS
    dist=[INF]*k
    dist[1]=0
    Q=deque([1])
    while(Q):
        v=Q.popleft()
        for nv,w in E[v]:
            if(dist[nv]<=dist[v]+w): continue
            dist[nv]=dist[v]+w
            if(w==0): Q.appendleft(nv)
            else: Q.append(nv)
    print(dist[0]+1)
resolve()
