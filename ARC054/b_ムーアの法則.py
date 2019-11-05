# https://atcoder.jp/contests/arc054/tasks/arc054_b
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    from math import log
    p=float(input())
    c=(log(2))/1.5
    if(c*p<=1):
        print(p)
    else:
        print((log(c)+log(p)+1)/c)
resolve()
