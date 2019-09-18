# https://atcoder.jp/contests/abc048/tasks/arc064_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    res=0
    for i in range(1,n):
        c=A[i]+A[i-1]-x
        if c>0:
            res+=c
            A[i]=max(A[i]-c,0)
    print(res)
resolve()
