# https://atcoder.jp/contests/abc127/tasks/abc127_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,m=map(int,input().split())
    L=-INF; R=INF
    for _ in range(m):
        l,r=map(int,input().split())
        L=max(L,l)
        R=min(R,r)
    print(max(R-L+1,0))
resolve()
