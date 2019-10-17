# https://atcoder.jp/contests/kupc2019/tasks/kupc2019_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,x=map(int,input().split())
    A=list(map(int,input().split()))
    m=max(A)
    print(sum(1 for i in range(n) if A[i]+x>=m))
resolve()
