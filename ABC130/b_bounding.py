# https://atcoder.jp/contests/abc130/tasks/abc130_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,x=map(int,input().split())
    L=list(map(int,input().split()))
    D=[0]*(n+1)
    for i in range(n):
        D[i+1]=D[i]+L[i]
    print(sum(D[i]<=x for i in range(n+1)))
resolve()
