# https://atcoder.jp/contests/agc018/tasks/agc018_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    A=[list(map(lambda x:int(x)-1,input().split())) for _ in range(n)]
    ans=INF

    for _ in range(m):
        C=[0]*m # スポーツのカウンター
        for i in range(n):
            for j in range(m):
                if(A[i][j] is not None):
                    C[A[i][j]]+=1
                    break
        M=max(C)
        ans=min(ans,M)
        ind=C.index(M)
        for i in range(n):
            for j in range(m):
                if(A[i][j]==ind):
                    A[i][j]=None

    print(ans)
resolve()
