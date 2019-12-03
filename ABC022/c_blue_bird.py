# https://atcoder.jp/contests/abc022/tasks/abc022_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        u,v,l=map(int,input().split())
        u-=1; v-=1
        E[u].append((v,l))
        E[v].append((u,l))

    # 最小コストの0 -> 0ループを見つけたい
    # (0,u)があるとして、uから0までの(0,u)を除いた最短距離を全て求める
    # pure DijkstraでO(n^3)
    def calc(x):
        assert(x!=0)
        dist=[INF]*n
        dist[x]=0
        calculated=[0]*n
        for _ in range(n-1):
            v=min((dist[v],v) for v in range(n) if(not calculated[v]))[1]
            calculated[v]=1
            for nv,l in E[v]:
                if((min(v,nv),max(v,nv))==(0,x)): continue
                if(dist[nv]>dist[v]+l):
                    dist[nv]=dist[v]+l
        return dist[0]

    ans=INF
    for x,l in E[0]:
        ans=min(ans,l+calc(x))
    print(ans if(ans!=INF) else -1)
resolve()
