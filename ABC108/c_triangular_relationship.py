# https://atcoder.jp/contests/abc108/tasks/arc102_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    n,k=map(int,input().split())
    if(k&1):
        s=n//k
        print(s**3)
    else:
        s=n//k
        t=(n+k//2)//k
        print(s**3+t**3)
resolve()
