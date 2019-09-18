# https://atcoder.jp/contests/abc035/tasks/abc035_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,q=map(int,input().split())
    imos=[0]*(n+1)
    for _ in range(q):
        l,r=map(int,input().split())
        imos[l-1]^=1
        imos[r]^=1
    imos.pop()
    for i in range(n-1):
        imos[i+1]^=imos[i]
    print(*imos,sep='')
resolve()
