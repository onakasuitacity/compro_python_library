# https://atcoder.jp/contests/abc105/tasks/abc105_d
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from collections import defaultdict
    n,m=map(int,input().split())
    A=list(map(int,input().split()))
    S=[0]*(n+1)
    for i in range(n):
        S[i+1]=S[i]+A[i]
    D=defaultdict(int)
    for s in S:
        D[s%m]+=1
    ans=0
    for val in D.values():
        ans+=val*(val-1)//2
    print(ans)
resolve()
