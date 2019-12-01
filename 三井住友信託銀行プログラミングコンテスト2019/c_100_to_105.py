# https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_c
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda:sys.stdin.readline().rstrip()
def resolve():
    x=int(input())
    for k in range(1,1001):
        if(100*k<=x<=105*k):
            print(1)
            return
    print(0)
resolve()
