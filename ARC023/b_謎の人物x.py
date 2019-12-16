# https://atcoder.jp/contests/arc023/tasks/arc023_2
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    h,w,d=map(int,input().split())
    G=[list(map(int,input().split())) for _ in range(h)]

    ans=0
    from itertools import product
    for i,j in product(range(h),range(w)):
        if(i+j>d): continue
        if((i+j+d)&1): continue
        ans=max(ans,G[i][j])

    print(ans)
resolve()
