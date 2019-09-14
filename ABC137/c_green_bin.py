# https://atcoder.jp/contests/abc137/tasks/abc137_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=sys.stdin.readline
def resolve():
    n=int(input())
    A=[0]*n
    for i in range(n):
        A[i]=''.join(sorted(input()))
    A.sort()
    from itertools import groupby
    ans=0
    for k,v in groupby(A):
        a=len(list(v))
        if a>=2: ans+=a*(a-1)//2
    print(ans)

resolve()
