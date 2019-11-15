# https://atcoder.jp/contests/abc092/tasks/abc092_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n=int(input())
    d,x=map(int,input().split())
    A=[int(input()) for _ in range(n)]
    ans=x
    for a in A:
        ans+=(d-1)//a+1
    print(ans)
resolve()
