# https://atcoder.jp/contests/apc001/tasks/apc001_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    k=n-m-1 # merge する回数
    if(k==0):
        print(0)
        return
    if(n<2*k):
        print("Impossible")
        return

    # cost の小さい方から使いたい
    A=[[a,i] for i,a in enumerate(map(int,input().split()))]
    A.sort()
    E=[[] for _ in range(n)]
    for _ in range(m):
        x,y=map(int,input().split())
        E[x].append(y)
        E[y].append(x)

    cnt=0
    col=[None]*n # 連結成分に分解
    def dfs(v)->bool:
        if(col[v] is not None): return False
        col[v]=cnt
        Q=[v]
        while(Q):
            v=Q.pop()
            for nv in E[v]:
                if(col[nv] is not None): continue
                col[nv]=cnt
                Q.append(nv)
        return True

    for v in range(n):
        cnt+=dfs(v)

    # 各連結成分(n-m 個)から1個ずつ選ぶ
    ans=0
    used=[0]*cnt
    for i in range(n):
        a,v=A[i]
        if(not used[col[v]]):
            ans+=a
            used[col[v]]=1
            A[i][0]=INF

    # 残りの頂点から 2k-(n-m) 個選ぶ
    A.sort()
    for a,v in A[:2*k-(n-m)]:
        ans+=a

    print(ans)
resolve()
