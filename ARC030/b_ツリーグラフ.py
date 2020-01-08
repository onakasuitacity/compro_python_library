# https://atcoder.jp/contests/arc030/tasks/arc030_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,x=map(int,input().split())
    x-=1
    H=list(map(int,input().split()))

    # コインが全く無ければ何もしない
    if(max(H)==0):
        print(0)
        return

    E=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[u].append(v)
        E[v].append(u)

    def dfs(v,p=-1):
        res=0
        for nv in E[v]:
            if(nv==p): continue
            d=dfs(nv,v)
            if(d==-1):
                res+=2
            elif(d>0):
                res+=d+2
        if(res>0):
            return res
        else:
            return -H[v]

    print(max(dfs(x),0))
resolve()
