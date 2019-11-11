# https://atcoder.jp/contests/chokudai_S002/tasks/chokudai_S002_k
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    A=[0]*n; B=[0]*n
    for i in range(n):
        A[i],B[i]=map(int,input().split())

    # coordinate compress
    C=sorted(set(A)|set(B))
    D={c:i for i,c in enumerate(C)}
    for i in range(n):
        A[i]=D[A[i]]
        B[i]=D[B[i]]

    N=2*n # 頂点数は最大で2*n
    E=[[] for _ in range(N)]
    for i in range(n):
        E[A[i]].append(B[i])
        E[B[i]].append(A[i])

    # dfs
    visited=[0]*N
    def dfs(v)->int:
        if(visited[v]): return 0
        visited[v]=1
        Q=[v]
        node=0
        deg=0
        while(Q):
            v=Q.pop()
            node+=1
            deg+=len(E[v])
            for nv in E[v]:
                if(visited[nv]): continue
                visited[nv]=1
                Q.append(nv)
        return min(node,deg//2)

    # output
    print(sum(dfs(v) for v in range(N)))
resolve()
