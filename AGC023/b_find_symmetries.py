# https://atcoder.jp/contests/agc023/tasks/agc023_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
from itertools import product

def resolve():
    n=int(input())
    G=[input() for _ in range(n)]
    ans=0
    for i in range(n):
        now=G[i:]+G[:i]
        ans+=all(now[i][j]==now[j][i] for i,j in product(range(n),repeat=2))

    print(n*ans)
resolve()
