# https://atcoder.jp/contests/abc131/tasks/abc131_f
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    V=100005
    n=int(input())
    E=[[] for _ in range(V*2)]
    for _ in range(n):
        x,y=map(int,input().split())
        y+=V
        E[x].append(y)
        E[y].append(x)

    visited=[0]*(2*V)
    def dfs(v):
        if(visited[v]): return
        visited[v]=1
        cnt[v//V]+=1
        for nv in E[v]: dfs(nv)

    ans=[0]
    for v in range(2*V):
        if(visited[v]): continue
        cnt=[0]*2 # 連結成分のx,yの個数
        dfs(v)
        ans[0]+=cnt[0]*cnt[1]
    print(ans[0]-n)
resolve()
