# https://atcoder.jp/contests/agc019/tasks/agc019_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    q,h,s,d=map(int,input().split())
    n=int(input())

    h=min(h,2*q)
    s=min(s,2*h)
    d=min(d,2*s)

    if(n&1):
        print(d*(n//2)+s)
    else:
        print(d*(n//2))
resolve()
