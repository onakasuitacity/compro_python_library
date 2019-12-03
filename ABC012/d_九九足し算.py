# https://atcoder.jp/contests/abc012/tasks/abc012_3
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    r=2025-int(input())
    for d in range(1,10):
        if(r%d==0 and r//d<=9):
            print("{} x {}".format(d,r//d))
resolve()
