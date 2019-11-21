# https://atcoder.jp/contests/abc087/tasks/arc090_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        u,v,w=map(int,input().split())
        u-=1; v-=1
        E[u].append((v,w))
        E[v].append((u,-w))

    pos=[INF]*n # position
    def dfs(v)->NoneType:
        if(pos[v]!=INF): return
        pos[v]=0
        Q=[v]
        while(Q):
            v=Q.pop()
            for nv,w in E[v]:
                if(pos[nv]==INF):
                    pos[nv]=pos[v]+w
                    Q.append(nv)
                else:
                    if(pos[nv]!=pos[v]+w):
                        print("No")
                        exit(0)

    for v in range(n): dfs(v)
    print("Yes")
resolve()
