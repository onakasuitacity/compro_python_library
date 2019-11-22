# https://atcoder.jp/contests/abc067/tasks/arc078_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    E=[[] for _ in range(n)]
    for _ in range(n-1):
        a,b=map(int,input().split())
        a-=1; b-=1
        E[a].append(b)
        E[b].append(a)

    # 0からn-1へのpathを求める
    path=[]
    def dfs(v,p=-1)->bool:
        if(v==n-1):
            path.append(v)
            return True
        for nv in E[v]:
            if(nv==p): continue
            if(dfs(nv,v)):
                path.append(v)
                return True
        return False
    dfs(0)
    path.reverse()
    k=len(path)
    a,b=path[(k+1)//2-1],path[(k+1)//2]

    # 辺a,bを削除する
    E[a].remove(b)
    E[b].remove(a)

    # このグラフに対して、0を含む連結成分の個数を求める
    from collections import deque
    Q=deque([0])
    visited=[0]*n
    while(Q):
        v=Q.popleft()
        visited[v]=1
        for nv in E[v]:
            if(visited[nv]): continue
            Q.append(nv)

    c=sum(visited)
    print("Fennec" if(c>n-c) else "Snuke")
resolve()
