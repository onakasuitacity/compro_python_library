# https://atcoder.jp/contests/abc144/tasks/abc144_a
import sys
sys.setrecursionlimit(2147483647)
INF=float("inf")
MOD=10**9+7
# input=lambda :sys.stdin.readline().rstrip()
def resolve():
    a,b=map(int,input().split())
    if(a>9 or b>9):
        print(-1)
    else:
        print(a*b)
resolve()
