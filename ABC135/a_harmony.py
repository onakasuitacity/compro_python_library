# https://atcoder.jp/contests/abc135/tasks/abc135_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    if((a+b)%2):
        print("IMPOSSIBLE")
    else:
        print((a+b)//2)
resolve()
