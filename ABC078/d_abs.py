# https://atcoder.jp/contests/abc078/tasks/arc085_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,z,w=map(int,input().split())
    A=list(map(int,input().split()))
    if(n==1):
        print(abs(A[0]-w))
    else:
        print(max(abs(A[-1]-w),abs(A[-2]-A[-1])))
resolve()
