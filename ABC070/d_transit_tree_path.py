# https://atcoder.jp/contests/abc070/tasks/abc070_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n=int(input())
    edges=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b,c=map(int,input().split())
        a-=1
        b-=1
        edges[a].append([b,c])
        edges[b].append([a,c])
    q,k=map(int,input().split())
    k-=1
    d=[INF]*n
    d[k]=0

    # dfs (root=k)
    Q=[[k,0]]
    while(Q):
        v,dist=Q.pop()
        for u,cost in edges[v]:
            if d[u]>dist+cost:
                d[u]=dist+cost
                Q.append([u,d[u]])

    for _ in range(q):
        x,y=map(lambda x:int(x)-1,input().split())
        print(d[x]+d[y])

resolve()
