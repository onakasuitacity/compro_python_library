# https://atcoder.jp/contests/chokudai_s001/tasks/chokudai_S001_l
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    perm=list(map(lambda x:int(x)-1,input().split()))

    visited=[0]*n
    def dfs(v)->bool:
        if(visited[v]): return False
        visited[v]=1
        Q=[v]
        while(Q):
            v=Q.pop()
            nv=perm[v]
            if(visited[nv]): break
            visited[nv]=1
            Q.append(nv)
        return Tru

    cnt=sum(dfs(v) for v in range(n))
    print("YES" if(cnt%2==0) else "NO")
resolve()
