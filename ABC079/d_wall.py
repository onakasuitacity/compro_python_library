# https://atcoder.jp/contests/abc079/tasks/abc079_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    h,w=map(int,input().split())
    C=[list(map(int,input().split())) for _ in range(10)]

    # Warshall-Floyd
    from itertools import product
    for k,i,j in product(range(10),repeat=3):
        C[i][j]=min(C[i][j],C[i][k]+C[k][j])

    # input
    A=[list(map(int,input().split())) for _ in range(h)]

    ans=0
    for i,j in product(range(h),range(w)):
        a=A[i][j]
        if(a==-1): continue
        ans+=C[a][1]
    print(ans)
resolve()
