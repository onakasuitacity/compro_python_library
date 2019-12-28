# https://atcoder.jp/contests/agc005/tasks/agc005_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7 # 998244353
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,x,y=map(int,input().split())
    x-=1; y-=1
    E1=[[] for _ in range(n)]
    E2=[[] for _ in range(n)]
    for _ in range(n-1):
        u,v=map(int,input().split())
        u-=1; v-=1
        E1[u].append(v)
        E1[v].append(u)
    for _ in range(n-1):
        u,v=map(int,input().split())
        u-=1; v-=1
        E2[u].append(v)
        E2[v].append(u)

    # E2 において、y-rooted tree とみて、depth,par を計算
    par=[None]*n # x の必勝頂点を判定するのに必要
    par[y]=y
    depth2=[None]*n
    depth2[y]=0
    Q=[y]
    while(Q):
        v=Q.pop()
        for nv in E2[v]:
            if(depth2[nv] is not None): continue
            depth2[nv]=depth2[v]+1
            par[nv]=v
            Q.append(nv)

    # E1の辺で、E2での距離が 3 以上のものは必勝
    win=[0]*n
    for v in range(n):
        for nv in E1[v]:
            if(par[v]==nv or par[nv]==v or par[v]==par[nv] or par[par[v]]==nv or par[par[nv]]==v): continue
            win[nv]=win[v]=1

    # E1 において、x-rooted tree とみて探索
    # depth1 < depth2 -> 以降も探索できる
    # depth1 = depth2 -> そこで捕まる
    ans=depth2[x]
    depth1=[None]*n
    depth1[x]=0
    Q=[x]
    while(Q):
        v=Q.pop()
        if(win[v]): # 探索できる状態 & 必勝頂点にいれば勝ち
            print(-1)
            return
        for nv in E1[v]:
            if(depth1[nv] is not None): continue
            depth1[nv]=depth1[v]+1
            ans=max(ans,depth2[nv])
            if(depth1[nv]<depth2[nv]): Q.append(nv)

    print(2*ans)
resolve()
