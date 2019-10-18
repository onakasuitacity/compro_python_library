# https://atcoder.jp/contests/abc142/tasks/abc142_f
# BFS (Warshall-FloydはC++でないと通らない)
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    E=[[] for _ in range(n)]
    for _ in range(m):
        a,b=map(lambda x:int(x)-1,input().split())
        E[a].append(b)
    # bfs
    def bfs(sv):
        prev=[-1]*n
        from collections import deque
        Q=deque([sv])
        while(Q):
            v=Q.popleft()
            for nv in E[v]:
                if(nv==sv):
                    break # for loop
                elif(prev[nv]==-1):
                    prev[nv]=v
                    Q.append(nv)
            else:
                continue
            break # while loop
        else:
            return [0]*(n+1)
        loop=[]
        while(v!=-1):
            loop.append(v)
            v=prev[v]
        loop.reverse()
        return loop
    # calculate
    ans=[0]*(n+1)
    for i in range(n):
        loop=bfs(i)
        if(len(loop)<len(ans)):
            ans=loop
    if(len(ans)==n+1):
        print(-1)
    else:
        print(len(ans))
        for v in ans: print(v+1)
resolve()
