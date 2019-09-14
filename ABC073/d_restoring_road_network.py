# https://atcoder.jp/contests/abc074/tasks/arc083_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n=int(input())
    A=[0]*n
    ans=0
    for i in range(n):
        A[i]=list(map(int,input().split()))
        ans+=sum(A[i])
    from copy import deepcopy
    B=deepcopy(A)
    # Warshall-Floyd
    from itertools import product
    for k,i,j in product(range(n),repeat=3):
        B[i][j]=min(B[i][j],B[i][k]+B[k][j])
    # calculate
    if A!=B:
        print(-1)
        return
    for i,j in product(range(n),repeat=2):
        if i==j: continue
        flag=False
        for r in range(n):
            if i==r or j==r: continue
            flag=(flag or B[i][j]==B[i][r]+B[r][j])
        if flag: ans-=B[i][j]
    print(ans//2)

resolve()
