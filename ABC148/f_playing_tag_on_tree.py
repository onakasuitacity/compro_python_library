# https://atcoder.jp/contests/abc148/tasks/abc148_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,x,y=map(int,input().split())
    x-=1; y-=1
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[u].append(v)
        E[v].append(u)

    # x,y それぞれの depth を計算する
    dx=[None]*n
    dx[x]=0
    Q=[(x,-1)]
    while(Q):
        v,p=Q.pop()
        for nv in E[v]:
            if(nv==p): continue
            dx[nv]=dx[v]+1
            Q.append((nv,v))

    dy=[None]*n
    dy[y]=0
    Q=[(y,-1)]
    while(Q):
        v,p=Q.pop()
        for nv in E[v]:
            if(nv==p): continue
            dy[nv]=dy[v]+1
            Q.append((nv,v))

    # x の方が y より近い点 v に対して、その1つ手前で捕まる
    ans=0
    for v in range(n):
        if(dx[v]<dy[v]):
            ans=max(ans,dy[v]-1)

    print(ans)
resolve()
