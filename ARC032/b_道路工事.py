# https://atcoder.jp/contests/arc032/tasks/arc032_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        u,v=map(int,input().split())
        u-=1; v-=1
        E[u].append(v)
        E[v].append(u)

    col=[None]*n
    cnt=0
    def dfs(v)->bool:
        if(col[v] is not None): return False
        Q=[v]
        col[v]=cnt
        while(Q):
            v=Q.pop()
            for nv in E[v]:
                if(col[nv] is not None): continue
                col[nv]=cnt
                Q.append(nv)
        return True

    for v in range(n):
        cnt+=dfs(v)

    print(cnt-1)
resolve()
