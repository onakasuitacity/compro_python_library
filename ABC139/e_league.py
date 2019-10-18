# https://atcoder.jp/contests/abc139/tasks/abc139_e
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from itertools import product
    n=int(input())
    match=[[0]*n for _ in range(n)]
    V=0 # V=n(n-1)/2
    for i,j in product(range(n),repeat=2):
        if(i>=j): continue
        match[i][j]=V
        V+=1

    def toID(i,j):
        if(i>j): i,j=j,i
        return match[i][j]

    E=[[] for _ in range(V)]
    for i in range(n):
        A=list(map(lambda x:int(x)-1,input().split()))
        for j in range(1,n-1):
            E[toID(i,A[j-1])].append(toID(i,A[j]))
    # 頂点数Vの有向グラフをdfsしてLongest pathの長さを求める
    # -1: unchecked, -2: checked and uncalculated
    dp=[-1]*V
    def dfs(v):
        if(dp[v]>=0): return
        dp[v]=-2
        length=0
        for nv in E[v]:
            if(dp[nv]==-2):
                print(-1)
                exit()
            if(dp[nv]==-1):
                dfs(nv)
            length=max(length,dp[nv]+1)
        dp[v]=length
    # calculate
    for i in range(V): dfs(i)
    print(max(dp)+1)
resolve()
