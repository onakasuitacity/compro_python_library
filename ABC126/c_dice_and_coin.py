# https://atcoder.jp/contests/abc126/tasks/abc126_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from math import log,ceil
    n,k=map(int,input().split())
    p=[0]*(n+1)
    for i in range(1,n+1):
        p[i]=max(0,ceil(log(k/i)/log(2)))
    ans=0
    for i in range(1,n+1):
        ans+=2**(-p[i])
    print(ans/n)
resolve()
