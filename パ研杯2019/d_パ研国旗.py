# https://atcoder.jp/contests/pakencamp-2019-day3/tasks/pakencamp_2019_day3_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product
def resolve():
    n=int(input())
    A=[list(input()) for _ in range(5)]
    col=['R','B','W']

    dp=[0]*3 # 0:R 1:B 2:W
    for j in range(n):
        ndp=[INF]*3
        for c,nc in product(range(3),repeat=2):
            if(c==nc): continue
            ndp[nc]=min(ndp[nc],dp[c]+sum(A[i][j]!=col[nc] for i in range(5)))
        dp=ndp

    print(min(dp))
resolve()
