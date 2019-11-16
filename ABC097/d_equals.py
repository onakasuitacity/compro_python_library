# https://atcoder.jp/contests/abc097/tasks/arc097_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    perm=list(map(lambda x:int(x)-1,input().split()))
    E=[[] for _ in range(n)]
    for _ in range(m):
        x,y=map(int,input().split())
        x-=1; y-=1
        E[x].append(y)
        E[y].append(x)

    # 連結成分ごとに分解する
    cnt=0
    comp=[-1]*n
    def dfs(v)->NoneType:
        global cnt
        if(comp[v]!=-1): return
        cnt+=1
        comp[v]=cnt[0]
        Q=[v]
        while(Q):
            v=Q.pop()
            for nv in E[v]:
                if(comp[nv]!=-1): continue
                comp[nv]=cnt[0]
                Q.append(nv)

    for v in range(n): dfs(v)
    print(sum(1 for v in range(n) if(comp[v]==comp[perm[v]])))
resolve()
