# https://atcoder.jp/contests/abc015/tasks/abc015_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=sys.stdin.readline
def resolve():
    n,k=map(int,input().split())
    A=[list(map(int,input().split())) for _ in range(n)]
    flag=True
    from itertools import product
    for Z in product(range(k),repeat=n):
        xor=0
        Z=list(Z)
        for i in range(n):
            xor^=A[i][Z[i]]
        if xor==0:
            flag=False
            break
    print("Nothing" if flag else "Found")
resolve()
